from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Product
from .cart import Cart 

def home(request):
    # 1. Get the search query from the URL (e.g., ?q=mango)
    query = request.GET.get('q')
    
    # 2. Filter products based on the query
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query), is_available=True)
    else:
        products = Product.objects.filter(is_available=True)

    cart = Cart(request)
    return render(request, 'shop/home.html', {'products': products, 'cart': cart})

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER', 'cart_detail'))

def cart_increment(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect(request.META.get('HTTP_REFERER', 'cart_detail'))

def cart_decrement(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.decrement(product=product)
    return redirect(request.META.get('HTTP_REFERER', 'cart_detail'))

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart(request)
    return render(request, 'shop/detail.html', {'product': product, 'cart': cart})

def about(request): return render(request, 'shop/about.html')
def contact(request): return render(request, 'shop/contact.html')