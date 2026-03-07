from rest_framework import serializers
from .models import User
import bcrypt # type: ignore

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, allow_blank=False)
    last_name = serializers.CharField(required=True, allow_blank=False)

    class Meta:
        model = User
        fields = ['email','first_name', 'last_name', 'password']  

        extra_kwargs = {
            'password': {'write_only': True}  # senha não aparece no retorno
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password= password,**validated_data)
        return user
        
    def validate_first_name(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("first_name deve ser uma string.")
        if not value.isalpha():
            raise serializers.ValidationError("first_name deve conter apenas letras, sem números ou símbolos.")
        return value

    def validate_last_name(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("last_name deve ser uma string.")
        if not value.isalpha():
            raise serializers.ValidationError("last_name deve conter apenas letras, sem números ou símbolos.")
        return value

    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

