from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class EmployeeManager(BaseUserManager):
    def create_user(self, email, name, password=None, role=""):
        if not email:
            raise ValueError("Users must have an email")
        user = self.model(email=self.normalize_email(email), name=name, role=role)
        user.set_password(password) # hash password
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Employees(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EmployeeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

class Customers(models.Model):
    name = models.TextField()
    email = models.EmailField(unique=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Transactions(models.Model):
    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal')
    ]

    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"
