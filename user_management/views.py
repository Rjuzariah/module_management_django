# views.py
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse
from .forms import UserForm
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
    user.delete()
    messages.success(request, 'User deleted successfully!')
    return redirect('user_list')
