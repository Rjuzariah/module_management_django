from django.db import models
from django.conf import settings
from django.core.management import call_command
from django.db.utils import OperationalError

class Module(models.Model):
    name = models.CharField(max_length=255, unique=True)
    version = models.CharField(max_length=50, default="1.0")
    is_installed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (v{self.version})"
    
    def install(self):
        # Check if the module is already installed
        if self.is_installed:
            print(f"Module {self.name} is already installed.")
            return

        # Mark the module as installed
        self.is_installed = True
        self.save()

        # Install the module logic (e.g., file copying, adding configs)
        print(f"Installing module: {self.name}")

        # Check if the app is in MODULE_APPS and run migrations if it is
        if self.name in settings.MODULE_APPS:
            try:
                # First, run makemigrations to generate migration files
                call_command('makemigrations', self.name)
                print(f"Migration files created for app: {self.name}")

                # Then, apply migrations
                call_command('migrate', self.name)
                print(f"Migration applied for app: {self.name}")
            except OperationalError as e:
                print(f"Failed to run migration for {self.name}: {e}")
            except Exception as e:
                print(f"An error occurred while installing {self.name}: {e}")
        else:
            print(f"App {self.name} not found in MODULE_APPS. Skipping migration.")

    def uninstall(self):
        # Simulate uninstalling the module
        self.is_installed = False
        self.save()

        # Add any uninstall logic here, like removing files, configurations, etc.
        print(f"Uninstalling module: {self.name}")
