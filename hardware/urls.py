from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.getHardware),
    path('create/',views.createHardware),
    path('update/<id_hw>',views.updateHardware, name='update'),
    path('delete/<id_hw>',views.deleteHardware, name='delete')
]
