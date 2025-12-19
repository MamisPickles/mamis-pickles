from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .cart import Cart 

# 1. HOMEPAGE
def home(request):
    products = Product.objects.filter(is_available=True)
    # CRITICAL: We must create the cart object here so the sidebar can see it!
    cart = Cart(request) 
    return render(request, 'shop/home.html', {'products': products, 'cart': cart})

# 2. ADD TO CART (Logic)
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    
    # CRITICAL: This sends the user back to the same page they came from
    return redirect(request.META.get('HTTP_REFERER', 'home'))

# 3. CART DETAIL PAGE
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})

# 4. REMOVE ITEM
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER', 'cart_detail'))

# 5. INCREMENT (+)
def cart_increment(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect(request.META.get('HTTP_REFERER', 'cart_detail'))

# 6. DECREMENT (-)
def cart_decrement(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.decrement(product=product)
    return redirect(request.META.get('HTTP_REFERER', 'cart_detail'))

# 7. PRODUCT DETAIL
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart(request) # Pass cart here too
    return render(request, 'shop/detail.html', {'product': product, 'cart': cart})

def about(request): return render(request, 'shop/about.html')
def contact(request): return render(request, 'shop/contact.html')