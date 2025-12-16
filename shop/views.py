from django.shortcuts import render, get_object_or_404
from .models import Product

# 1. Homepage
def home(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'shop/home.html', {'products': products})

# 2. Product Detail
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'shop/detail.html', {'product': product})

# 3. About Page
def about(request):
    return render(request, 'shop/about.html')

# 4. Contact Page (This is the one you were missing)
def contact(request):
    return render(request, 'shop/contact.html')