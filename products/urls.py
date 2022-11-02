from django.urls import path

from products import views

app_name = 'products'
urlpatterns = [
    path('', view=views.products, name='product-list'),
    path('add', view=views.create_products, name='product-add'),
]