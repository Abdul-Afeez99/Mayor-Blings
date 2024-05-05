from django.urls import path 
from .views import (CreateCategory, CreateProduct, UpdateCategory, 
                    UpdateProduct, DeleteCategory, DeleteProduct)

urlpatterns = [
    path('category/create', CreateCategory.as_view(), name='create_category'),
    path('product/create', CreateProduct.as_view(), name='create_product'),
    path('category/update', UpdateCategory.as_view(), name='update_category'),
    path('product/update', UpdateProduct.as_view(), name='update_product'),
    path('category/delete', DeleteCategory.as_view(), name='delete_category'),
    path('product/delete', DeleteProduct.as_view(), name='delete_product'),
]
