from django.shortcuts import render,redirect
from hardware.models import Hardware
from .forms import HardwareForm

# Create your views here.
def getHardware(request):
    obj = Hardware.objects.all()
    if obj:
        data = {'hw':obj}
    else:
        data = {}
    return render(request,'../templates/hardware/index.html',data)

def createHardware(request):
    if request.method == 'POST':
        form = HardwareForm(request.POST)
        if form.is_valid():
            vendorName = form.cleaned_data['vendorName']
            vendorModel = form.cleaned_data['hardwareName']
            hardware = Hardware(hardwareVendor=vendorName,hardwareModel=vendorModel)
            hardware.save()
        return redirect('/hardware')
    else:
        form = HardwareForm()
    return render(request,'../templates/hardware/create_hw.html',{'form':form})

def updateHardware(request,id_hw):
    print(id_hw)
    context = {
        'data':id_hw
    }
    return render(request,'../templates/hardware/edit_hw.html',context)

def deleteHardware(request,id_hw):
    hardware = Hardware.objects.get(id=id_hw)
    print(hardware)
    hardware.delete()
    return redirect('/hardware')
 