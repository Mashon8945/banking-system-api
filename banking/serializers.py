from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Employees

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Employees.objects.create_user(
            username=validated_data['username'],
            email = validated_data['email'],
            password= validated_data['password'],
            role = validated_data.get('role', '')
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Credentials")