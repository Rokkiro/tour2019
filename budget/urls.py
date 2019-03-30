from django.urls import path
from . import views
from django.contrib import admin

app_name = 'budget'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
<<<<<<< HEAD
=======
    path('cash/', views.CashView.as_view(), name='cash'),
>>>>>>> 13eef93d9354183026c45e3aab371adffe5d01cb
    path('admin/', views.adminView, name='admin'),
]