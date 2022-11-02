from django.urls import path

from products import views

app_name = 'products'
urlpatterns = [
    path('products', view=views.products, name='products_list'),
    path('product/add', view=views.create_products, name='product_add'),
]