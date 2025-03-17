from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    PRODUCT_CATEGORIES = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('books', 'Books'),
        ('home', 'Home & Kitchen'),
    ]

    product_category = forms.ChoiceField(choices=PRODUCT_CATEGORIES, required=False)

    class Meta:
        model = Product
        fields = ['name', 'barcode', 'price', 'stock', 'product_category']
