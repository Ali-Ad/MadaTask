from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=64)
    period = models.CharField(max_length=64)

    def __str__(self):
        return self.name
