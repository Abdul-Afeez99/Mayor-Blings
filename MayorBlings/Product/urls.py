from django.urls import path
from .views import (ListAllCategories, ListAllProducts, ListAllProductsInCategory,
                    GetCategoryById, GetProductById)

urlpatterns = [
    path('categories', ListAllCategories.as_view(), name='list_all_categories'),
    path('products', ListAllProducts.as_view(), name='list_all_products'),
    path('category/products', ListAllProductsInCategory.as_view(), name='list_all_products_in_category'),
    path('categories/category', GetCategoryById.as_view(), name='get_category_by_id'),
    path('products/product', GetProductById.as_view(), name='get_product_by_id'),
]
