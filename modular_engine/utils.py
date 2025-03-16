# modular_engine/utils.py
from django.conf import settings
from modular_engine.models import Module

def create_module_data(**available_module):

    # Check if the module already exists in the database
    module, created = Module.objects.update_or_create(
            name=available_module["name"], # Lookup condition
            defaults={
                "verbose_name": available_module["verbose_name"],
                "icon": available_module["icon"],
            }
        )
    print(f"Module '{module.verbose_name}' created/updated successfully.")
