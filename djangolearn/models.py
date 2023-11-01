from django.db import models


# Create your models here.
class Location(models.Model):
    country = models.CharField(max_length=15),
    timezone = models.CharField(max_length=10),
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.country
