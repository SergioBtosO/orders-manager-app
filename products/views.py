from django.contrib import messages
from itertools import product
from django.shortcuts import render

from products.models import Product
from products.forms import ProductForm

# Create your views here.
def create_products(request):
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if product_form.is_valid():
            data = product_form.cleaned_data
            actual_objects = Product.objects.filter(
                name=data["name"], id=data["id"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El producto {data['name']} - {data['id']} ya existe",
                )
            else:
                product = Product(name=data["name"], id=data["id"])
                product.save()
                messages.success(
                    request,
                    f"producto {data['name']} - {data['id']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"products": Product.objects.all()},
                template_name="products/products_list.html",
            )

    product_form = ProductForm(request.POST)
    context_dict = {"form": product_form}
    return render(
        request=request,
        context=context_dict,
        template_name="products/products_form.html",
    )
def products(request):
    return render(
        request=request,
        context={"products": Product.objects.all()},
        template_name="product/product_list.html",
    )
