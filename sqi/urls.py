from django.contrib import admin
from django.urls import path
from sqi import views

urlpatterns = [
    path('sqi/', views.sqi_home, name ='sqi' ),
    path('new/', views.addform, name = 'added'),
    path('paid/<int:todo_id>', views.paid, name = 'paid'),
    path('delete_paid/', views.deletepaid, name = 'delete_paid'),
    path('delete_unpaid/', views.deleteunpaid, name = 'delete_unpaid'),
    path('deletealll/', views.deleteall, name = 'deletealll'),
]
