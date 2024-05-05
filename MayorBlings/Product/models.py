from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=50)
    category_description = models.TextField()
    category_image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name
    
    
class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    product_image = models.URLField()
    product_quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_name
