# module_engine/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.module_list, name='module_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
