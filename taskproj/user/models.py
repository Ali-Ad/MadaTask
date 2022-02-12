from django.db import models

class User(models.Model):

    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.username
