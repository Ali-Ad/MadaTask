from django.db import models

class Employee(models.Model):
    username=models.CharField(max_length=64)
    password=models.CharField(max_length=64)

    def __str__(self):
        return self.username
