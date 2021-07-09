from django.db import models


class Addresses(models.Model):
    userId = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=13)
    name = models.CharField(max_length=13)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]


# Create your models here.
