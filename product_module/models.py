from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    product_category = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.name
    
    class Meta:
        app_label = "product_module"
