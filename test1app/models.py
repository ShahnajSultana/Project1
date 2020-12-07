from django.db import models

# Create your models here.
class Friends(models.Model):
    name = models.CharField(max_length = 250)
    age = models.IntegerField()
    address = models.CharField(max_length = 250)

