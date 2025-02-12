from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Customers, Transactions

User = get_user_model()

class EmployeeTests(APITestCase):
    def test_register_employee(self):
        url = reverse('register_employee')
        data = {
            'name': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'role': 'manager'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'testuser')

    def test_login_employee(self):
        url = reverse('login_employee')
        User.objects.create_user(name='testuser', email='testuser@example.com', password='testpassword')
        data = {
            'name': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)

class CustomerTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(name='testuser', email='testuser@example.com', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_add_customer(self):
        url = reverse('add_customer')
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'account_balance': '1000.00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customers.objects.count(), 1)
        self.assertEqual(Customers.objects.get().name, 'John Doe')

    def test_list_customers(self):
        Customers.objects.create(name='John Doe', email='johndoe@example.com', account_balance='1000.00')
        url = reverse('list_customers')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'John Doe')

class TransactionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(name='testuser', email='testuser@example.com', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.customer = Customers.objects.create(name='John Doe', email='johndoe@example.com', account_balance='1000.00')

    def test_deposit_money(self):
        url = reverse('deposit_money')
        data = {
            'customer': self.customer.id,
            'transaction_type': 'deposit',
            'amount': '500.00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.account_balance, 1500.00)

    def test_withdraw_money(self):
        url = reverse('withdraw_money')
        data = {
            'customer': self.customer.id,
            'transaction_type': 'withdrawal',
            'amount': '500.00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.account_balance, 500.00)

    def test_withdraw_money_insufficient_funds(self):
        url = reverse('withdraw_money')
        data = {
            'customer': self.customer.id,
            'transaction_type': 'withdrawal',
            'amount': '1500.00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.account_balance, 1000.00)