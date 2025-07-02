from django.urls import path, include
from . import views

urlpatterns = [
    path('chatapp/', views.chatapp, name = 'chatapp'),
    path('screening/', views.screening, name = 'screening')
    
]