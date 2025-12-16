from django.db import models

# Create your models here.
from django.db import models

# 1. CATEGORY TABLE (e.g., "Spicy Pickles", "Sweet Pickles")
class Category(models.Model):
    name = models.CharField(max_length=50) 

    def __str__(self):
        return self.name

# 2. PRODUCT TABLE (The actual Jar)
class Product(models.Model):
    # The name of the pickle (e.g., "Mami's Cut Mango")
    name = models.CharField(max_length=100) 
    
    # Links this pickle to a Category (If "Spicy" is deleted, this logic decides what happens)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    # The Price (DecimalField is better than Float for money to avoid math errors)
    # max_digits=6 means prices up to 9999.99
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    
    # The details (Ingredients, storage info)
    description = models.TextField() 
    
    # The Photo (Requires the 'Pillow' library we installed)
    image = models.ImageField(upload_to='products/') 
    
    # Stock Status (Uncheck this in Admin to hide product if sold out)
    is_available = models.BooleanField(default=True)
    
    # Auto-saves the date when you add the product
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name