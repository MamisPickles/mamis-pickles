from django.contrib import admin
from .models import Category, Product, ProductImage

# 1. CREATE THE GALLERY INLINE
# This allows uploading extra images inside the Product page
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Shows 1 empty slot by default (click "Add" for more)

# 2. CUSTOMIZE THE PRODUCT ADMIN
class ProductAdmin(admin.ModelAdmin):
    # Add the gallery inline here
    inlines = [ProductImageInline]
    
    # Optional: Shows these columns in the product list
    list_display = ('name', 'price', 'category', 'is_available')

# 3. REGISTER MODELS
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
# You can also register ProductImage separately if you want to see them as a list
admin.site.register(ProductImage)