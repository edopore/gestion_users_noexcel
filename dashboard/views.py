from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def holaMundo(request):
    return HttpResponse("Hola Mundo")

def holaMundoHtml(request):
    return render(request,'index.html',None)