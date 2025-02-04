from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from authentication.manager import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["user_name", "name"]