# user_management/urls.py
from django.urls import path
from .views import UserListView, UserCreateView, UserEditView, UserDeleteView, UserLoginView, UserLogoutView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/edit/<int:pk>/', UserEditView.as_view(), name='user_edit'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path("login/", UserLoginView.as_view(), name="user_login"),
    path("logout/", UserLogoutView.as_view(), name="user_logout"),
]