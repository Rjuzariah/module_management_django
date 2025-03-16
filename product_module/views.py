from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect
from user_management.utils import CustomLoginRequiredMixin


# List view for products
class ProductListView(CustomLoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = 'product_module/list.html'
    context_object_name = 'products'
    permission_required = 'product_module.view_product'

# Detail view for a single product
class ProductDetailView(CustomLoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    template_name = 'product_module/detail.html'
    context_object_name = 'product'
    permission_required = 'product_module.view_product'

# Create view for creating a new product
class ProductCreateView(CustomLoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_module/form.html'
    permission_required = 'product_module.add_product'
    success_url = reverse_lazy('product_list')

# Update view for updating an existing product
class ProductUpdateView(CustomLoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_module/form.html'
    permission_required = 'product_module.change_product'
    context_object_name = 'product'  # Access the product instance in the template

    def get_success_url(self):
        # Redirect to the product list after a successful update
        return reverse_lazy('product_list')
    
# Delete view for deleting a product
class ProductDeleteView(CustomLoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_module/confirm_delete.html'
    permission_required = 'product_module.delete_product'
    success_url = reverse_lazy('product_list')

    # Overriding the post method to ensure product deletion happens only via POST request
    def post(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()
        return redirect(self.success_url)
