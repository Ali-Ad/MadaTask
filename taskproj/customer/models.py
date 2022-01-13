from django.db import models
from service.models import Service

class Customer(models.Model):
    fullname=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=64)
    customerservices=models.ManyToManyField(Service)
    

