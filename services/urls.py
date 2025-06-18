from django.urls import path
from . import views

urlpatterns = [
    path('mark-completed/<int:pk>/', views.mark_completed, name='mark_completed'),
    path('mark-uncompleted/<int:pk>/', views.mark_uncompleted, name='mark_uncompleted'),
   
]