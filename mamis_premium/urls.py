from django.contrib import admin
from django.urls import path
from shop import views  # Import your shop views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Main Pages
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # --- CART & CHECKOUT LINKS ---
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    # --- NEW LINKS FOR (+) AND (-) BUTTONS ---
    path('cart/increment/<int:product_id>/', views.cart_increment, name='cart_increment'),
    path('cart/decrement/<int:product_id>/', views.cart_decrement, name='cart_decrement'),
]

# This allows images to appear (Debug mode only)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)