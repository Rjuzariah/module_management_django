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
        try:
            with open(OPTIONAL_APPS_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([self.name])

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
    def uninstall(self):

        print(f"Uninstalling module: {self.name}")

        print(f"Cleaning up table for: {self.name}")
        call_command("migrate")


        # Simulate uninstalling the module
        self.is_installed = False
        self.save()
        self.remove_installed_app(self.name)

        print(f"Finish uninstalling module: {self.name}")


    def remove_installed_app(app_name):
        """Remove an installed app from the CSV file."""
        if not os.path.exists(OPTIONAL_APPS_FILE):
            return

        # Read existing apps
        with open(OPTIONAL_APPS_FILE, "r") as f:
            apps = [row[0] for row in csv.reader(f) if row]

        # Remove the specified app
        apps = [app for app in apps if app != app_name]

        # Write updated list back to the file
        with open(OPTIONAL_APPS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            for app in apps:
                writer.writerow([app])
