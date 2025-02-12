from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import login

from .serializers import UserSerializer, LoginSerializer, CustomerSerializer
from .models import Customers


@api_view(['POST'])
def register_employee(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def login_employee(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return Response({"message": "Login is successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def add_customer(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def list_customers(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    customers = Customers.objects.all()

    sort_by = request.query_params.get('sort_by', 'id')
    order = request.query_params.get('order', 'asc')

    if order == 'desc':
        sort_by = f'--{sort_by}'
    customers = customers.order_by(sort_by)

    filtered_customers = paginator.paginate_queryset(customers, request)
    serializer = CustomerSerializer(filtered_customers, many=True)
    return paginator.get_paginated_response(serializer.data)
