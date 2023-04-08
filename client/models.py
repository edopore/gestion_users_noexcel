from tabnanny import verbose
from django.db import models

# Create your models here.
class Client(models.Model):
    fullName = models.CharField(max_length=50, null=False, blank=False)
    documentId = models.CharField(primary_key=True,max_length=20, unique=True, null=False, blank=False)
    
    def __str__(self):
        return self.fullName
        