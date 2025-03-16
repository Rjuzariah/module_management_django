# urls.py
from django.urls import path
from .views import ModuleListView, ModuleActionView, DashboardView

urlpatterns = [
    path('', ModuleListView.as_view(), name='module_list'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('module/<int:module_id>/action/', ModuleActionView.as_view(), name='module_action'),
]