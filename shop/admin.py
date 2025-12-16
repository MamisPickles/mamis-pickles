from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product

# This tells Django: "Show these tables on the Admin Page"
admin.site.register(Category)
admin.site.register(Product)