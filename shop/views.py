from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .cart import Cart  # Importing the cart logic

# 1. Homepage
def home(request):
    products = Product.objects.filter(is_available=True)
    # IMPORTANT: We pass the 'cart' to the template so the sidebar can access it
    cart = Cart(request) 
    return render(request, 'shop/home.html', {'products': products, 'cart': cart})

# 2. Product Detail
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart(request) # Pass cart here too just in case
    return render(request, 'shop/detail.html', {'product': product, 'cart': cart})

# 3. About Page
def about(request):
    return render(request, 'shop/about.html')

# 4. Contact Page
def contact(request):
    return render(request, 'shop/contact.html')

# 5. Add to Cart Logic
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    
    # CHANGED: Stay on the same page!
    return redirect(request.META.get('HTTP_REFERER', 'home'))

# 6. Remove from Cart Logic
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    
    # CHANGED: Stay on the same page!
    return redirect(request.META.get('HTTP_REFERER', 'cart_detail'))

# 7. Cart Page Display
def cart_detail(request):
    cart = Cart(request)
    
    # Generate the WhatsApp Message with the full order list
    whatsapp_msg = "Hello Mami's, I would like to place an order:%0a"
    for item in cart:
        whatsapp_msg += f"- {item['product'].name} (x{item['quantity']}): ₹{item['total_price']}%0a"
    whatsapp_msg += f"%0a*Total Amount: ₹{cart.get_total_price()}*"

    return render(request, 'shop/cart.html', {'cart': cart, 'whatsapp_msg': whatsapp_msg})

# 8. INCREMENT (+1)
def cart_increment(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    
    # CHANGED: Stay on the same page!
    return redirect(request.META.get('HTTP_REFERER', 'cart_detail'))

# 9. DECREMENT (-1)
def cart_decrement(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.decrement(product=product)
    
    # CHANGED: Stay on the same page!
    return redirect(request.META.get('HTTP_REFERER', 'cart_detail'))