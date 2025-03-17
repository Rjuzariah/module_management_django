import os
import csv
from django.db import models
from django.conf import settings
from django.core.management import call_command
from django.db.utils import OperationalError

OPTIONAL_APPS_FILE = os.path.join(settings.BASE_DIR, "installed_apps.csv")

class Module(models.Model):
    name = models.CharField(max_length=255, unique=True)
    verbose_name = models.CharField(max_length=255, unique=True)
    icon = models.CharField(max_length=255, default="icons/default_icon.png")  
    is_installed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (v{self.version})"
    
    def run_migrations(self):
        # First, run makemigrations to generate migration files
        call_command('makemigrations', self.name)
        print(f"Migration files created for app: {self.name}")

        # Then, apply migrations
        call_command('migrate', self.name)
        print(f"Migration applied for app: {self.name}")
    
    def install(self):
        # Check if the module is already installed
        if self.is_installed:
            print(f"Module {self.name} is already installed.")
            return

        # Install the module logic
        print(f"Installing module: {self.name}")
        try:
            self.run_migrations()

            # Mark the module as installed
            self.is_installed = True
            self.save()
        except OperationalError as e:
            print(f"Failed to run migration for {self.name}: {e}")
        except Exception as e:
            print(f"An error occurred while installing {self.name}: {e}")

    def upgrade(self):
        # Check if the module is already installed
        if not self.is_installed:
            print(f"Module {self.name} is not installed, please install first to proceed.")
            return

        # Install the module logic
        print(f"Updating module: {self.name}")
        try:
            self.run_migrations()
            
        except OperationalError as e:
            print(f"Failed to run migration for {self.name}: {e}")
        except Exception as e:
            print(f"An error occurred while installing {self.name}: {e}")

    def uninstall(self):

        print(f"Uninstalling module: {self.name}")
        # Simulate uninstalling the module
        self.is_installed = False
        self.save()

        print(f"Finish uninstalling module: {self.name}")