from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.management import call_command
from .models import Module
from .serializers import ModuleSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    @action(detail=True, methods=["post"])
    def install(self, request, pk=None):
        module = self.get_object()
        if module.is_installed:
            return Response({"message": "Module already installed"}, status=status.HTTP_400_BAD_REQUEST)

        module.is_installed = True
        module.save()
        call_command("migrate", "example_module")  # Run migrations for the module
        return Response({"message": f"Module {module.name} installed successfully"})

    @action(detail=True, methods=["post"])
    def upgrade(self, request, pk=None):
        module = self.get_object()
        if not module.is_installed:
            return Response({"message": "Module is not installed"}, status=status.HTTP_400_BAD_REQUEST)

        # Auto-generate and apply migrations for the module
        call_command("makemigrations", module.name)  # Generate migrations dynamically
        call_command("migrate", module.name)  # Apply migrations

        return Response({"message": f"Module {module.name} upgraded successfully"})


    @action(detail=True, methods=["post"])
    def uninstall(self, request, pk=None):
        module = self.get_object()
        if not module.is_installed:
            return Response({"message": "Module is not installed"}, status=status.HTTP_400_BAD_REQUEST)

        module.is_installed = False
        module.save()
        return Response({"message": f"Module {module.name} uninstalled successfully"})
