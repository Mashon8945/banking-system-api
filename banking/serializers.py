from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Employees, Customers, Transactions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['name', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Employees.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            password= validated_data['password'],
            role = validated_data.get('role', '')
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Credentials")
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['name', 'email', 'account_balance', 'created_at', 'updated_at']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['customer', 'transaction_type', 'amount', 'created_at', 'updated_at']