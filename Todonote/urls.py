from django.contrib import admin
from django.urls import path
from Todonote import views

urlpatterns = [
    path('', views.index, name ='index' ),
    path('add/', views.addform, name = 'add'),
    path('completed/<int:todo_id>', views.completed, name = 'completed'),
    path('delete_completed/', views.deletecompleted, name = 'delete_completed'),
    path('deleteall/', views.deleteall, name = 'deleteall'),
]