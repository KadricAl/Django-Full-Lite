from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('technician', 'Technician'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25, blank=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.username} - {self.city}'