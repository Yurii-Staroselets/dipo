from django.db import models


class Storehouse(models.Model):
    name_store = models.CharField(max_length=255)
    street_store = models.CharField(max_length=255)

    def __str__(self):
        return self.name_store
# Create your models here.
