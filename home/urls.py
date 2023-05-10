from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('auther_and_seller/', views.auther_and_seller, name='auther_and_seller'),
   path('upload_books/', views.upload_books, name='upload_books'),
   path('my_books/', views.my_books, name='my_books'),
]
