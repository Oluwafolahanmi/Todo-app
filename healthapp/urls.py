from django.contrib import admin
from django.urls import path
from healthapp import views

urlpatterns = [
    path('healthapp/', views.home_health, name ='healthapp' ),
    path('register/', views.add, name = 'register'),
    path('Discharged/', views.discharge, name = 'Discharged'),
    # path('deleteall/', views.deleteall, name = 'deleteall'),
]