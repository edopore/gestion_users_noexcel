from django.shortcuts import render
from django.http import HttpResponse
from service.models import Service

# Create your views here.
def holaMundo(request):
    obj = Service.objects.all()
    if obj:
        data = {'data':'no such data'}
    else:
        data = {'data':obj}
    return render(request,'../templates/dashboard/index.html',data)