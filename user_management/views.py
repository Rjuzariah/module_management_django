# views.py
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import UserForm, LoginForm
# List users
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_management/list.html', {'users': users})

# Create a user
def user_create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')
            return redirect('user_list')
    else:
        form = UserCreationForm()
    return render(request, 'user_management/user_form.html', {'form': form})

# Edit a user
def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_management/user_form.html', {'form': form, 'user': user})

# Delete a user
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('user_list')
    return render(request, 'user_management/confirm_delete.html', {'user': user})


def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")  # Change this to your desired redirect page
            else:
                form.add_error(None, "Invalid username or password.")
    
    return render(request, "user_management/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("user_login")
