from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.getService),
    path('create/',views.createService),
    path('update/',views.updateService),
    path('delete/',views.deleteService)
]
