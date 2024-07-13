from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.TextField()
    category_image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name
    
    
class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_name

class ProductImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.URLField()
    