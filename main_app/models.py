from django.db import models
from django.urls import reverse
# Create your models here.
class Widget(models.Model):
    quantity = models.IntegerField(blank=True,null=True)
    description = models.CharField(blank=True,null=True,max_length=100)
    
    def get_absolute_url(self):
        return reverse('widget_delete', kwargs={ 'pk': self.id })
