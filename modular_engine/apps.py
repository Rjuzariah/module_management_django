from django.apps import AppConfig



class ModularEngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modular_engine'

    def ready(self):
        from . import utils

        # Register the signal to create modules during application startup
        utils.create_module_data()
