from django.db import models

class Service(models.Model):
    sname=models.CharField(max_length=50)
    sprice=models.CharField(max_length=64)
    speriod=models.CharField(max_length=64)


