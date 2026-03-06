from rest_framework import serializers
from .models import User
import bcrypt # type: ignore

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','first_name', 'last_name', 'password']  # só email e senha

        extra_kwargs = {
            'password': {'write_only': True}  # senha não aparece no retorno
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password= password,**validated_data)
        return user
        

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

