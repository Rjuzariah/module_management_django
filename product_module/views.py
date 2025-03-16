from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import permission_required

@permission_required("product_module.view_product", raise_exception=True)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_module/list.html', {'products': products})

@permission_required("product_module.view_product", raise_exception=True)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_module/detail.html', {'product': product})

@permission_required("product_module.add_product", raise_exception=True)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_module/form.html', {'form': form})

@permission_required("product_module.change_product", raise_exception=True)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_module/form.html', {'form': form})

@permission_required("product_module.delete_product", raise_exception=True)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_module/confirm_delete.html', {'product': product})
