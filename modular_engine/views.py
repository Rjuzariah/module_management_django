# module_engine/views.py
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Module
from user_management.utils import CustomLoginRequiredMixin


class ModuleListView(CustomLoginRequiredMixin, ListView):
    model = Module
    template_name = 'modular_engine/list.html'
    permission_required = 'modular_engine.view_module'
    context_object_name = 'modules'

    def post(self, request, *args, **kwargs):
        """
        Handles the install/uninstall actions from the POST request.
        """
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

class ModuleActionView(CustomLoginRequiredMixin, View):
    permission_required = 'modular_engine.change_module'
    """
    Handles the install, uninstall, and upgrade actions for a module.
    Redirects back to the module list page with success/error messages.
    """
    def post(self, request, module_id):
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
                module.upgrade()
                messages.success(request, f"Module '{module.name}' upgraded successfully.")
            else:
                messages.error(request, "Module must be installed before upgrading.")

        else:
            messages.error(request, "Invalid action.")

        return redirect("module_list")

class DashboardView(CustomLoginRequiredMixin, View):
    """
    Displays the dashboard page with installed modules.
    Only visible to admin or manager users.
    """
    def get(self, request, *args, **kwargs):
        # Fetch installed modules
        modules = Module.objects.filter(is_installed=True)
        is_manager_or_admin = request.user.is_staff or request.user.groups.filter(name="manager").exists()
        return render(request, 'modular_engine/dashboard.html', {'modules': modules, 'is_manager_or_admin': is_manager_or_admin})
