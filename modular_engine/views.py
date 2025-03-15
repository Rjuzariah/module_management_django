# module_engine/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Module
from django.shortcuts import get_object_or_404, redirect, render

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

def module_action(request, module_id):
    """
    Handles install, uninstall, and upgrade actions for a module.
    Redirects back to the module list page with success/error messages.
    """
    module = get_object_or_404(Module, id=module_id)
    action = request.POST.get("action")

    if action == "install":
        if not module.is_installed:
            module.install()
            messages.success(request, f"Module '{module.name}' installed successfully!")
        else:
            messages.error(request, "Module is already installed.")

    elif action == "uninstall":
        if module.is_installed:
            module.uninstall()
            messages.success(request, f"Module '{module.name}' uninstalled successfully!")
        else:
            messages.error(request, "Module is not installed.")

    elif action == "upgrade":
        if module.is_installed:
            # module.version = "1.1"  # Example: Set a new version
            # module.save()
            messages.success(request, f"Module '{module.name}' upgraded successfully.")
        else:
            messages.error(request, "Module must be installed before upgrading.")

    else:
        messages.error(request, "Invalid action.")

    return redirect("module_list") 

def dashboard(request):
    # Fetch installed modules
    modules = Module.objects.filter(is_installed=True)
    return render(request, 'modular_engine/dashboard.html', {'modules': modules})
