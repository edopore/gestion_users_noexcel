from pydoc import doc
from django.shortcuts import render,redirect
from .models import Client
# Create your views here.
def getClient(request):
    obj = Client.objects.all()
    data = {'client':obj}
    return render(request,'../templates/client/index.html',data)

def createClient(request):
    if request.method == 'POST':
        print(request.POST)
        fullName = request.POST.get('client-fullName')
        documentId = request.POST.get('client-id')
        client = Client(fullName=fullName,documentId=documentId)
        client.save()
        return redirect(getClient)
    else:
        return render(request,'../templates/client/create-client.html',None)

def updateClient(request,id_client):
    client = Client.objects.get(documentId=id_client)
    if request.method == 'POST':
        print(request.POST)
        fullName = request.POST.get('client-fullName')
        client.fullName = fullName
        client.save()
        return redirect(getClient)
    else:
        context = {
            'data':client,
        }
        return render(request,'../templates/client/edit_client.html',context)

def deleteClient(request,id_client):
    client = Client.objects.get(documentId=id_client)
    client.delete()
    return redirect(getClient)

 