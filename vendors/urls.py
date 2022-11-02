from django.urls import path

from vendors import views

app_name = 'vendors'

urlpatterns = [
    path('', view=views.vendors,name='vendor-list'),
    path('add',view=views.create_vendor,name='vendor-add'),
]