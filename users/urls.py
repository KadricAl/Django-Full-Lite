from django.urls import path
from . import views

urlpatterns = [
    path('technician/dashboard/', views.technician_dashboard, name='technician_dashboard'),
    path('technician/all-devices/', views.technician_all_devices, name='technician_all_devices'),
    path('technician/all-requests/', views.technician_all_requests, name='technician_all_requests'),
    path('technician/all-services/', views.technician_all_services, name='technician_all_services'),
    path('client/dashboard/', views.client_dashboard, name='client_dashboard'),
    path('client/my_devices/', views.client_my_devices, name='client_my_devices'),
    path('client/requests/', views.client_requests, name='client_requests'),
    path('client/all-services/', views.client_all_services, name='client_all_services'),
]