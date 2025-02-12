from django.urls import path

from .views import *

urlpatterns = [
    path('employees/register/', register_employee, name='register_employee'),
    path('employee/login/', login_employee, name='login_employee'),
    path('customers/', add_customer, name='add_customer'),
    path('customers/', list_customers, name='list_customers'),
]