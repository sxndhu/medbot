from django.urls import path, include
from . import views

urlpatterns = [
    path('checksymptom/', views.checksymptom, name = 'checksymptom'),

]