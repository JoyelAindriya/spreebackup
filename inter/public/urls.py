from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('manage',views.manage_site,name='manage'),
    path('reg',views.reg,name='reg'),
    path('login',views.login,name='login')
]