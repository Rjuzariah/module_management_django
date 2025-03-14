# module_engine/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Module

def module_list(request):
    modules = Module.objects.all()

    if request.method == "POST":
        module_name = request.POST.get('module_name')
        action = request.POST.get('action')

        try:
            module = Module.objects.get(name=module_name)

            if action == "install" and not module.is_installed:
                module.install()
                messages.success(request, f"Module '{module_name}' installed successfully!")
            elif action == "uninstall" and module.is_installed:
                module.uninstall()
                messages.success(request, f"Module '{module_name}' uninstalled successfully!")
            else:
                messages.error(request, f"Module '{module_name}' is already in the desired state.")
        except Module.DoesNotExist:
            messages.error(request, "Module not found!")

        return redirect('module_list')

    return render(request, 'modular_engine/list.html', {'modules': modules})

def dashboard(request):
    # Fetch installed modules
    modules = Module.objects.filter(is_installed=True)
    return render(request, 'modular_engine/dashboard.html', {'modules': modules})
