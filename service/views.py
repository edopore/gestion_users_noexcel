from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getService(request):
    return HttpResponse('get service')

def createService(request):
    return HttpResponse('create service')

def updateService(request):
    return HttpResponse('update service')

def deleteService(request):
    return HttpResponse('delete service')
 