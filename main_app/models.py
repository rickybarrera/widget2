from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class Widget(models.Model):
    quantity = models.IntegerField()
    description = models.CharField(max_length=100)