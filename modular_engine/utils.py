# # modular_engine/utils.py
# from django.conf import settings
# from modular_engine.models import Module

# def create_module_data(**available_module):
#     """
#     Ensures that a Module is created for every app listed in INSTALLED_APPS,
#     except for system apps like django.contrib.*.
#     """
#     print("")
#     print("")
#     print("")
#     print("")
#     print(available_module)

#     # Check if the module already exists in the database
#     module, created = Module.objects.update_or_create(
#             name=available_module["name"], # Lookup condition
#             defaults={
#                 "name_display": available_module["name_display"],
#                 "icon": available_module["icon"],
#             }
#         )
#     print(f"Module '{module.name_display}' created/updated successfully.")

# # import os
# # import importlib

# # PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))  # Root of your Django project

# # def find_available_modules():
# #     available_modules = []

# #     for root, dirs, files in os.walk(PROJECT_DIR):
# #         if "apps.py" in files:
# #             module_path = os.path.relpath(root, PROJECT_DIR).replace(os.sep, ".")
# #             try:
# #                 app_config_module = importlib.import_module(f"{module_path}.apps")
# #                 for attr in dir(app_config_module):
# #                     app_config = getattr(app_config_module, attr)
# #                     if isinstance(app_config, type) and hasattr(app_config, "is_application"):
# #                         available_modules.append({
# #                             "name": app_config.name,
# #                             "name_display": app_config.name_display,
# #                             "icon": app_config.icon,
# #                         })
# #             except (ModuleNotFoundError, AttributeError) as e:
# #                 print(f"Skipping module {module_path} due to error: {e}")
# #                 continue  # Skip invalid apps

# #     return available_modules



# from django.apps import AppConfig
# from django.db.migrations.loader import MigrationLoader
# from django.db import connection

# def skip_migration(app_name):
#     """Removes migrations for the given app_name if it is not installed."""
#     from modular_engine.models import Module  # Import your Module model dynamically

#     try:
#         module = Module.objects.get(name=app_name)
#         if not module.is_installed:
#             # Modify Django's migration loader to exclude this module
#             connection.ensure_connection()
#             loader = MigrationLoader(connection)
#             loader.disk_migrations = {
#                 key: migration for key, migration in loader.disk_migrations.items()
#                 if key[0] != app_name
#             }
#             print(f"Skipping migrations for {app_name} (not installed)")
#     except Module.DoesNotExist:
#         print(f"Module {app_name} not found in database. Skipping migration check.")
