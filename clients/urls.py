from django.urls import path

from clients import views

app_name = 'clients'
urlpatterns = [
    path('', view=views.clients, name='client-list'),
    path('add', view=views.create_client, name='client-add'),
]
