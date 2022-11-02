from django.contrib import messages
from django.shortcuts import render

from products.models import Product
from products.forms import ProductForm

# Create your views here.


def create_products(request):
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            data = product_form.cleaned_data
            actual_objects = Product.objects.filter(
                name=data["name"], ref=data["ref"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El producto {data['name']} - {data['ref']} ya existe",
                )
            else:
                product = Product(name=data["name"],  ref=data["ref"], description=data["description"], price=data["price"], weight=data["weight"],
                size=data["size"], colors=data["colors"],)
                product.save()
                messages.success(
                    request,
                    f"producto {data['name']} - {data['ref']} creado exitosamente!",
                )

            products = Product.objects.all()
            context_dict = {"products": products}
            return render(
                request, 'product_list.html',
                context_dict,)

    return render(request, 'product_form.html', {
        'form': ProductForm
    })

def products(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {'products': products})
