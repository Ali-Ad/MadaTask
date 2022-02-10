from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    price = models.CharField(max_length=64 )
    period = models.CharField(max_length=64 )
    description=models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Service"

