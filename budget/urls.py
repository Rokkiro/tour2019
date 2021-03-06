from django.urls import path
from . import views
from django.contrib import admin

app_name = 'budget'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('cash/', views.CashView.as_view(), name='cash'),
    path('admin/', views.adminView, name='admin'),
]