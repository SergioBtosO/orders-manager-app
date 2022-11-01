from django.contrib import messages
from itertools import product
from django.shortcuts import render

from clients.models import Client
from clients.forms import ClientForm

# Create your views here.
def create_clients(request):
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if client_form.is_valid():
            data = client_form.cleaned_data
            actual_objects = Client.objects.filter(
                name=data["name"], id=data["id"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El cliente {data['name']} - {data['id']} ya existe",
                )
            else:
                client = Client(name=data["name"], id=data["id"])
                client.save()
                messages.success(
                    request,
                    f"cliente {data['name']} - {data['id']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"clients": Client.objects.all()},
                template_name="clients/clients_list.html",
            )

    client_form = ClientForm(request.POST)
    context_dict = {"form": client_form}
    return render(
        request=request,
        context=context_dict,
        template_name="clients/clients_form.html",
    )
def clients(request):
    return render(
        request=request,
        context={"clients": Client.objects.all()},
        template_name="clients/client_list.html",
    )

