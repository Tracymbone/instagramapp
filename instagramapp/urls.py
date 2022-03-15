# from atexit import register
# from unicodedata import name
from django.shortcuts import render
from django.urls import path,include
from instagramapp import views
urlpatterns = [
    
    path('',views.home,name='home' ),
     path('login/', views.login,name='login'),
    path('register/', views.register,name='register'),
    path('project/', views.project,name='project'),
    
]