from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

class CustomPermissionRequiredMixin(PermissionRequiredMixin):
    def handle_no_permission(self):
        # Return a Forbidden response or your custom behavior
        return HttpResponseForbidden("You do not have permission to access this page.")

# Base class with centralized login_url
class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/user_management/login/'
