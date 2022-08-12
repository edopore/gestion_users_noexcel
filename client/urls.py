from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.getClient),
    path('create/',views.createClient),
    path('update/',views.updateClient),
    path('delete/',views.deleteClient)
]
