from django.contrib import admin
from django.urls import path, include 
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('feedback',views.feedback,name='feedback'),
    path('login',views.loginUser,name='login'),
    path('login.html',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout')

]
