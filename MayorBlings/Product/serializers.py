from .models import Categories, Products, ProductImages
from rest_framework import serializers

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        
class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=200)
    product_name = serializers.CharField(max_length=200)
    product_description = serializers.CharField(max_length=10000)
    product_quantity = serializers.IntegerField()
    product_price = serializers.DecimalField(max_digits=15, decimal_places=2)
    images = serializers.ListField(child=serializers.URLField())
    
    class Meta:
        model = Products
        fields = [
            'category', 
            'product_name', 
            'product_description', 
            'product_quantity', 
            'product_price', 
            'images'
        ]
        
    def save(self, **kwargs):
        category_obj = Categories.objects.get(category_name = self.validated_data['category'])
        product = Products(
            category = category_obj.id,
            product_name = self.validated_data['product_name'],
            product_description = self.validated_data['product_description'],
            product_quantity = self.validated_data['product_quantity'],
            product_price = self.validated_data['product_price']
        )
        product.save()
        for image in self.validated_data['images']:
            ProductImages.objects.create(
                product = product,
                image = image
            )
