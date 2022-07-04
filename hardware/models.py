from pyexpat import model
from django.db import models

# Create your models here.
class Hardware(models.Model):
    hardwareVendor = models.CharField(max_length=20)
    hardwareModel = models.CharField(max_length=20)

    def __str__(self):
        return self.serialNumber
