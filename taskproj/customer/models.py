from tkinter.tix import STATUS
from django.db import models
from service.models import Service


class Customer(models.Model):
    name = models.CharField(max_length=50, unique=True, default="")
    identity_number = models.CharField(max_length=9)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=64)
    address = models.CharField(max_length=64)
    location = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer"


class CustomerService(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    period = models.CharField(max_length=24, default="")
    Status = models.BooleanField(default=False)
    discount = models.CharField(max_length=24, default="")
    info = models.CharField(max_length=64, default="")

    class Meta:
        verbose_name = "Customer-service"
