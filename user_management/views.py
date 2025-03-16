from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import UserForm
from user_management.utils import CustomPermissionRequiredMixin
# from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.contrib import messages

# User List View
class UserListView(CustomPermissionRequiredMixin, ListView):
    model = User
    template_name = 'user_management/list.html'
    context_object_name = 'user_datas'
    permission_required = 'auth.view_user'

# User Create View
class UserCreateView(CustomPermissionRequiredMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'user_management/user_form.html'
    permission_required = 'auth.add_user'
    success_url = '/user_management/users/'

# User Edit View
class UserEditView(UpdateView):
    model = User
    template_name = 'user_management/user_form.html'
    form_class = UserForm
    success_url = '/user_management/users/'

    def get_object(self, queryset=None):
        # Ensure we're editing the correct user and not modifying the logged-in user
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        # Call the parent method to get the default context data
        context = super().get_context_data(**kwargs)
        # Add the user being edited as 'user_data'
        context['user'] = self.request.user
        context['user_data'] = self.get_object()  # This gets the user being edited
        return context


# User Delete View
class UserDeleteView(CustomPermissionRequiredMixin, DeleteView):
    model = User
    template_name = 'user_management/confirm_delete.html'
    permission_required = 'auth.delete_user'
    success_url = '/user_management/users/'

    def get_object(self, queryset=None):
        # Ensure we're editing the correct user and not modifying the logged-in user
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        # Call the parent method to get the default context data
        context = super().get_context_data(**kwargs)
        # Add the user being edited as 'user_data'
        context['user'] = self.request.user
        context['user_data'] = self.get_object()  # This gets the user being edited
        return context

class UserLoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'user_management/login.html'
    success_url = '/module/dashboard'  # Replace with the actual redirect URL after login

    def get_form_kwargs(self):
        # Pass the request to the form kwargs
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request  # Attach the request to the form
        return kwargs

    def form_valid(self, form):
        # Authenticate and log the user in
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid username or password.")
            return self.form_invalid(form)

from django.contrib.auth.views import LogoutView

class UserLogoutView(LogoutView):
    next_page = 'user_login'  # Redirect to the login page after logout
