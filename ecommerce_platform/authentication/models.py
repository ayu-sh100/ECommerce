from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django_otp.models import Device

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set', 
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class OTPDevice(Device):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)