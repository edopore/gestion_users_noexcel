from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.getClient,name='view-clients'),
    path('create/',views.createClient,name='create-client'),
    path('update/<id_client>',views.updateClient,name='update-client'),
    path('delete/<id_client>',views.deleteClient,name='delete-client')
]
