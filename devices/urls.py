from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_device, name='add_device'),
    path('<int:pk>/delete/', views.delete_device, name='delete_device'),
    path('<int:pk>/edit/', views.edit_device, name='edit_device'),
]
