from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.getHardware),
    path('create/',views.createHardware),
    path('update/',views.updateHardware),
    path('delete/',views.deleteHardware)
]
