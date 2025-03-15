from django.apps import AppConfig


class ProductModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_module'
    name_display = 'Product'
    is_module = True
    icon = 'icons/product_icon.png'

    # def ready(self):
    #     from modular_engine import utils
    #     utils.skip_migration(app_name=self.name)
    #     # from modular_engine import utils

    #     # # Register the signal to create modules during application startup
    #     # utils.create_module_data(name=self.name, name_display=self.name_display, icon=self.icon)

