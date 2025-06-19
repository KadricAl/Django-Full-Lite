from django.urls import path
from . import views

urlpatterns = [
    path('mark-completed/<int:pk>/', views.mark_completed, name='mark_completed'),
    path('mark-uncompleted/<int:pk>/', views.mark_uncompleted, name='mark_uncompleted'),
    path('client/request-service/<int:device_id>/', views.request_service, name='client_request_service'),
    path('client/cancel-request/<int:service_id>/', views.cancel_service_request, name='client_cancel_service'),
   
]