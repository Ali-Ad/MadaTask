from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50 , default="")
    price = models.CharField(max_length=64 , default="")
    period = models.CharField(max_length=64 , default="")
    description=models.CharField(max_length=64 , default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Service"

