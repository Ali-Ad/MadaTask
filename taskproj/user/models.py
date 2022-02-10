from django.db import models

class User(models.Model):

    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, default='')
    is_active = models.BooleanField(null=True)

    def __str__(self):
        return self.username
