from django.shortcuts import render
from .models import Client
# Create your views here.
def getClient(request):
    obj = Client.objects.all()
    if obj:
        data = {'client':obj}
    else:
        data = {}
    return render(request,'../templates/client/index.html',data)

def createClient(request):
    pass

def updateClient(request):
    pass

def deleteClient(request):
    pass
 