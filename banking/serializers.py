from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Employees, Customers, Transactions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['name', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return Employees.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            password= validated_data['password'],
            role = validated_data.get('role', '')
        )
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)

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