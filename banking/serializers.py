from rest_framework import serializers
from django.contrib.auth import authenticate
from  django.contrib.auth import get_user_model

from .models import Employees, Customers, Transactions

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Employees.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            role = validated_data.get('role', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['name', 'email', 'account_balance', 'created_at', 'updated_at']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['customer', 'transaction_type', 'amount', 'created_at', 'updated_at']