from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from .views import *

urlpatterns = [
    path('employee/register', register_employee, name='register_employee'),
    path('employee/login', login_employee, name='login_employee'),

    path('customers/add', add_customer, name='add_customer'),
    path('customers', list_customers, name='list_customers'),
    path('customers/<int:customer_id>', delete_customer, name='delete_customer'),

    path('transactions/deposit', deposit_money, name='deposit_name'),
    path('transactions/withdraw', withdraw_money, name='withdraw_money'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_pair'),

]