from django.urls import path

from clients import views

app_name = 'clients'
urlpatterns = [
    path('clients/', view=views.clients, name='client_list'),
    path('client/add', view=views.create_client, name='client_add'),
]
