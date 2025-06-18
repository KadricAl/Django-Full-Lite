from django.db import models
from datetime import timedelta
from users.models import CustomUser
from django.utils import timezone

class Device(models.Model):
    
    STATUS_CHOICES =[
        ('installed', 'Installed'),
        ('deactivated', 'Deactivated'),
        ('in_progress', 'In progress'),
    ]
    serial_number = models.CharField(max_length=20, unique=True)
    device_type = models.CharField(max_length=100)
    device_brand = models.CharField(max_length=100)
    installation_date = models.DateField(default=timezone.now)
    warranty_expiry = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='installed')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='devices')
    
    def save(self, *args, **kwargs):
        if self.installation_date and not self.warranty_expiry:
            self.warranty_expiry = self.installation_date + timedelta(days=365)
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f'{self.serial_number} - {self.installation_date}'
    
