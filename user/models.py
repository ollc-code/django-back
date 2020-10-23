from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.db import models

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 100, unique = True)
    name = models.CharField(max_length = 100, blank = True)
    email = models.EmailField()
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    date_joined = models.DateTimeField(auto_now = True)

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def __str__(self):
        return self.name