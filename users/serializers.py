from rest_framework import serializers
from .models import User
import bcrypt # type: ignore

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def create(self, validated_data):
            hashed = bcrypt.hashpw(validated_data['password'].encode('utf-8'), bcrypt.gensalt())
            validated_data['password'] = hashed.decode('utf-8')
            return User.objects.create_user(**validated_data)
        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
