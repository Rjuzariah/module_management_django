# modular_engine/utils.py
from django.conf import settings
from modular_engine.models import Module

def create_module_data():
    """
    Ensures that a Module is created for every app listed in INSTALLED_APPS,
    except for system apps like django.contrib.*.
    """
    module_app = settings.MODULE_APPS

    for module_name in module_app:

        # Check if the module already exists in the database
        module, created = Module.objects.get_or_create(name=module_name)

        if created:
            print(f"Module '{module_name}' created successfully.")
        else:
            print(f"Module '{module_name}' already exists.")
