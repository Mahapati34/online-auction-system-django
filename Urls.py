from django.contrib import admin
from django.urls import import path
import views
from django.contrib.auth import (
    import views as auth_views)
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register,
         name='register'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('items/logout', views.logout,
         name='logout'),
    path('myprofile', views.myprofile,
         name='myprofile'),
    path('future', views.future, name='future'),
    path('log', views.log, name='log'),
]
