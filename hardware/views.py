from django.shortcuts import render,redirect
from hardware.models import Hardware
from .forms import HardwareForm

# Create your views here.
def getHardware(request):
    obj = Hardware.objects.all()
    data = {'hw':obj}
    return render(request,'../templates/hardware/index.html',data)

def createHardware(request):
    if request.method == 'POST':
        print(request.POST)
        form = HardwareForm(request.POST)
        if form.is_valid():
            vendorName = form.cleaned_data['hardwareVendor']
            vendorModel = form.cleaned_data['hardwareModel']
            hardware = Hardware(hardwareVendor=vendorName,hardwareModel=vendorModel)
            hardware.save()
        return redirect('/hardware')
    else:
        form = HardwareForm()
    return render(request,'../templates/hardware/create_hw.html',{'form':form})

def updateHardware(request,id_hw):
    hardware = Hardware.objects.get(id=id_hw)
    if request.method == 'POST':
        vendorName = request.POST.get('hardware-vendor')
        vendorModel = request.POST.get('hardware-model')
        hardware.hardwareVendor = vendorName
        hardware.hardwareModel = vendorModel
        hardware.save()
        return redirect('/hardware')
    else:
        context = {
            'data':hardware,
        }
        return render(request,'../templates/hardware/edit_hw.html',context)

def deleteHardware(request,id_hw):
    hardware = Hardware.objects.get(id=id_hw)
    print(hardware)
    hardware.delete()
    return redirect('/hardware')
