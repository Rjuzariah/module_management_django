from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ProductModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_module'
    verbose_name = 'Product'
    is_module = True
    icon = 'icons/product_icon.png'
    default_url = 'product:product_list'

    def ready(self):
        post_migrate.connect(self.setup_modules, sender=self)

    def setup_modules(self, sender, **kwargs):
        from modular_engine import utils
        """Call utility function to create module data after migrations."""
        utils.create_module_data(name=self.name, verbose_name=self.verbose_name, icon=self.icon)

