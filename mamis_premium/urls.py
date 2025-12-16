from django.contrib import admin
from django.urls import path
from shop import views  # Import your shop views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='detail'),
    path('about/', views.about, name='about'),
    
    # NEW LINE
    path('contact/', views.contact, name='contact'),
]
# This part allows images to appear (Debug mode only)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)