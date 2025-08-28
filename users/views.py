from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User
from .serializers import RegisterSerializer, LoginSerializer
import bcrypt # type: ignore
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.utils.http import urlsafe_base64_decode

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"messsage": "Usuário registrado com sucesso! " },status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    
    user = authenticate(username=username, password=password)

    if user is not None:
        from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response({'error': 'Usuário ou senha inválidos'}, status=401)


token_generator = PasswordResetTokenGenerator()

@api_view(["POST"])
def forgot_password(request):
    email = request.data.get("email")
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "Usuário não encontrado"}, status=404)

    token = token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    reset_link = f"http://localhost:3000/reset-password/{uid}/{token}/"

    # Exemplo: envia por email
    send_mail(
        "Redefinir senha",
        f"Clique no link para redefinir sua senha: {reset_link}",
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )

    return Response({"message": "Email de recuperação enviado"})


@api_view(['POST'])
def reset_password(request,uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk = uid)
    except (User.DoesNotExist, ValueError, TypeError):
        return Response({'error': "Usuario não encontrado"}, status = status.HTTP_404_NOT_FOUND)
    
    if not token_generator.check_token(user, token):
        return Response({'error': "Token invalido ou expirado"}, status = status.HTTP_400_BAD_REQUEST)
    
    new_password = request.data.get('password')
    if not new_password:
        return Response({'error': "A nova senha é obrigatoria"}, status = status.HTTP_400_BAD_REQUEST)
    
    user.set_password(new_password)
    user.save()
    
    return Response({'message': "Senha alterada com sucesso"}, status=status.HTTP_200_OK)


