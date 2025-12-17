from django.db import models

# 1. CATEGORY TABLE
class Category(models.Model):
    name = models.CharField(max_length=50) 

    def __str__(self):
        return self.name

# 2. PRODUCT TABLE (Main Product Info)
class Product(models.Model):
    name = models.CharField(max_length=100) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    description = models.TextField() 
    
    # This is the MAIN thumbnail image
    image = models.ImageField(upload_to='products/') 
    
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 3. PRODUCT IMAGE TABLE (Gallery for Extra Photos) -- ADD THIS SECTION
class ProductImage(models.Model):
    # This links the image to a specific Product
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    # This uploads the extra photos to a 'gallery' folder
    image = models.ImageField(upload_to='product_gallery/')

    def __str__(self):
        return f"Image for {self.product.name}"