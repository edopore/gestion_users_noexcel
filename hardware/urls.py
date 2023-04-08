from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.getHardware,name='view-hw'),
    path('create/',views.createHardware,name='create-hw'),
    path('update/<id_hw>',views.updateHardware, name='update-hw'),
    path('delete/<id_hw>',views.deleteHardware, name='delete-hw')
]
