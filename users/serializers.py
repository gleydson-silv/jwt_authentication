from rest_framework import serializers
from .models import User
import bcrypt # type: ignore

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']  # só email e senha

        extra_kwargs = {
            'password': {'write_only': True}  # senha não aparece no retorno
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # usa o hash interno do Django
        user.save()
        return user
        

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

