from django.contrib import messages
from django.shortcuts import render

from clients.models import Client
from clients.forms import ClientForm

def clients(request):
    clients = Client.objects.all()
    context_dict = {"clients": clients}
    return render(
        request, 'client_list.html',
        context_dict,

    )


def create_client(request):
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            data = client_form.cleaned_data
            actual_objects = Client.objects.filter(
                name=data["name"], nit=data["nit"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El cliente {data['name']} - {data['nit']} ya existe",
                )
            else:
                client = Client(name=data["name"], nit=data["nit"],phone=data['phone'], email=data['email'], address=data['address'],)
                client.save()
                messages.success(
                    request,
                    f"cliente {data['name']} - {data['nit']} creado exitosamente!",
                )

            clients = Client.objects.all()
            context_dict = {"clients": clients}
            return render(
                request, 'client_list.html',
                context_dict,)

    return render(request, 'client_form.html', {
        'form': ClientForm
    })