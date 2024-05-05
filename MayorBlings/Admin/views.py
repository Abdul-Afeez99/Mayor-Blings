from rest_framework import generics, permissions, response, status
from Product.models import Categories, Products
from Product.serializers import CategoriesSerializer, ProductsSerializer
from Authentication.permissions import IsAdmin
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Create categories view
class CreateCategory(generics.GenericAPIView):
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.IsAuthenticated & IsAdmin]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)   

# Create products view   
class CreateProduct(generics.GenericAPIView):
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated & IsAdmin]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

# Update category view
class UpdateCategory(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated & IsAdmin]
    serializer_class = CategoriesSerializer
    # generate the swagger documentation for the patch method
    @swagger_auto_schema(
        operation_description="Update category details",
        manual_parameters=[
            openapi.Parameter(
                name="category_id",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Category ID",
                required=True
            )
        ])
    
    def patch(self, request):
        category_id = self.request.query_params.get('category_id')
        category = Categories.objects.get(id=category_id)
        serializer = self.serializer_class(category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)

# Update product view     
class UpdateProduct(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated & IsAdmin]
    serializer_class = ProductsSerializer
    
    # generate the swagger documentation for the patch method
    @swagger_auto_schema(
        operation_description="Update product details",
        manual_parameters=[
            openapi.Parameter(
                name="product_id",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Product ID",
                required=True
            )
        ])
    def patch(self, request):
        product_id = self.request.query_params.get('product_id')
        product = Products.objects.get(id=product_id)
        serializer = self.serializer_class(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)

# Delete category view   
class DeleteCategory(APIView):
    permission_classes = [permissions.IsAuthenticated & IsAdmin]
    # generate the swagger documentation for the delete method
    @swagger_auto_schema(
        operation_description="Delete category detail",
        manual_parameters=[
            openapi.Parameter(
                name="category_id",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Category ID",
                required=True
            )
        ])
    def delete(self, request):
        category_id = self.request.query_params.get('category_id')
        category = Categories.objects.get(id=category_id)
        category.delete()
        return response.Response({"message": "Category deleted successfully"}, status=status.HTTP_200_OK)

# Delete product view   
class DeleteProduct(APIView):
    permission_classes = [permissions.IsAuthenticated & IsAdmin]
    
    @swagger_auto_schema(
        operation_description="Delete category detail",
        manual_parameters=[
            openapi.Parameter(
                name="product_id",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Product ID",
                required=True
            )
        ])
    def delete(self, request):
        product_id = self.request.query_params.get('product_id')
        product = Products.objects.get(id=product_id)
        product.delete()
        return response.Response({"message": "Product deleted successfully"}, status=status.HTTP_200_OK)