from django.shortcuts import render
from django.contrib import messages

from vendors.models import Vendor
from vendors.forms import VendorForm

# Create your views here.


def create_vendor(request):
    if request.method == 'POST':
        vendor_form = VendorForm(request.POST)
        if vendor_form.is_valid():
            data = vendor_form.cleaned_data
            actual_objects = Vendor.objects.filter(
                name=data['name'], document=data['document']).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request, f"Vendedor {data['name']} - {data['document']} ya existe",)
            else:
                vendor = Vendor(name=data['name'], document=data['document'],
                                phone=data['phone'], email=data['email'], address=data['address'],)
                vendor.save()
                messages.success(
                    request, f"Vendedor {data['name']} - data={data['document']} creado con exito!",)

            return render(request=request, context={'vendors': Vendor.objects.all()}, template_name="vendor_list.html")

    return render(request, 'vendor_form.html', {
        'form': VendorForm
    })


def vendors(request):
    vendors = Vendor.objects.all()
    return render(request, "vendor_list.html", {'vendors': vendors})
