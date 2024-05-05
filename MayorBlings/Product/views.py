from django.shortcuts import render
from rest_framework import generics, permissions, response, status
from .models import Categories, Products
from .serializers import CategoriesSerializer, ProductsSerializer
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# List all categories view
class ListAllCategories(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.AllowAny]
    
# List all products view    
class ListAllProducts(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.AllowAny]

# List all products in a category view
class ListAllProductsInCategory(APIView):
    permission_classes = [permissions.AllowAny]
    # generate the swagger documentation for the get method
    @swagger_auto_schema(
        operation_description="Get all products in a category",
        manual_parameters=[
            openapi.Parameter(
                name="category_id",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Category ID",
                required=True
            )],
     )
    
    def get(self, request):
        category_id = self.request.query_params.get('category_id')
        products = Products.objects.filter(category=category_id)
        product_list = []
        for product in products:
            product_list.append({
                "name": product.product_name,
                "description": product.product_description,
                "image": product.product_image,
                "quantity": product.product_quantity,
                "price": product.product_price
            })
        return response.Response(product_list, status=status.HTTP_200_OK)

# Get category by ID view
class GetCategoryById(APIView):
    permission_classes = [permissions.AllowAny]
    # generate the swagger documentation for the get method
    @swagger_auto_schema(
        operation_description="Get category by ID",
        manual_parameters=[
            openapi.Parameter(
                name="category_id",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Category ID",
                required=True
            )],
        responses={status.HTTP_200_OK: openapi.Response("Applicant details", schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING, description="name of the category"),
                "description": openapi.Schema(type=openapi.TYPE_STRING, description="desccription of the category"),
                "image": openapi.Schema(type=openapi.TYPE_STRING, description="Link to the category image"),
            }
        ))}
    )
    def get(self, request):
        category_id = self.request.query_params.get('category_id')
        category_obj = Categories.objects.get(id=category_id)
        return response.Response({
            "name": category_obj.category_name,
            "description": category_obj.category_description,
            "image": category_obj.category_image
            }, status=status.HTTP_200_OK)  

# Get product by ID view      
class GetProductById(APIView):
    permission_classes = [permissions.AllowAny]
    # generate the swagger documentation for the get method
    @swagger_auto_schema(
        operation_description="Get product by ID",
        manual_parameters=[
            openapi.Parameter(
                name="product_id",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Product ID",
                required=True
            )],
        responses={status.HTTP_200_OK: openapi.Response("Applicant details", schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING, description="name of the product"),
                "description": openapi.Schema(type=openapi.TYPE_STRING, description="desccription of the product"),
                "image": openapi.Schema(type=openapi.TYPE_STRING, description="Link to the product image"),
                "quantity": openapi.Schema(type=openapi.TYPE_INTEGER, description="product quantity"),
                "price": openapi.Schema(type=openapi.TYPE_NUMBER, description="product price")
            }
        ))}
    )
    def get(self, request):
        product_id = self.request.query_params.get('product_id')
        product_obj = Products.objects.get(id=product_id)
        return response.Response({
            "name": product_obj.product_name,
            "description": product_obj.product_description,
            "image": product_obj.product_image,
            "quantity": product_obj.product_quantity,
            "price": product_obj.product_price
            }, status=status.HTTP_200_OK)   