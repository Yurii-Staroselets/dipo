from django.db import models
from storehouse.models import Storehouse


class Worker(models.Model):
    full_name = models.CharField(max_length=255)
    storehouse = models.ForeignKey(Storehouse, on_delete=models.CASCADE, related_name="worker")
    position = models.CharField(max_length=255)
    worker_login = models.CharField(max_length=255)
    worker_password = models.CharField(max_length=255)
    cashier = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)
    salary = models.IntegerField()

# Create your models here.
