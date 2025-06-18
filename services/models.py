from django.db import models
from django.utils import timezone
from users.models import CustomUser
from devices.models import Device

class Service(models.Model):
    
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished'),
        ('canceled', 'Canceled'),
    ]
    
    TYPE_CHOICES = [
        ('R', 'Requested service'),
        ('Y', 'Yearly service'),
        ('N', 'N service'),
        ]
    
    service_type = models.CharField(max_length=10, choices=TYPE_CHOICES,)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    request_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    client_desc = models.TextField(max_length=500, blank=True, null=True)
    tech_desc = models.TextField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='services')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='services')
    
    def __str__(self):
        return f'{self.device}({self.status}) - {self.request_date}'
