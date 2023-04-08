from django.db import models
from client.models import Client
from hardware.models import Hardware

# Create your models here.
# Add client 'n hardware later
class Service(models.Model):
    serviceClient = models.ForeignKey(Client, on_delete=models.CASCADE, default=0)
    hardwareService = models.OneToOneField(Hardware, on_delete=models.CASCADE, default=0)
    servicePhone = models.CharField(max_length=10)
    servicePhone2 = models.CharField(max_length=10)
    serviceEmail = models.EmailField(default="nomail@mail.com")
    serviceAddress = models.CharField(max_length=50)
    typeOfService = models.CharField(max_length=20)
    subscriptionPlan = models.CharField(max_length=10)
    serialNumberHardwareService = models.CharField(max_length=20, default="XXXXXXXXXXXXXXXXXXXX")
    ipAddress = models.CharField(max_length=15,default='')
    macAddress = models.CharField(max_length=12,default='')
    subscriptionDate = models.DateField()
    subscriptionDateInstalation = models.DateField()
    unsubscribeDateService = models.DateField()

    def __str__(self):
        return self.serviceClient+': '+self.ipAddress
