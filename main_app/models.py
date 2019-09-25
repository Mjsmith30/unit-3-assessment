from django.db import models
from django.urls import reverse


class Item(models.Model):
    description = models.CharField(max_length=100)
       
def get_absolute_url():
    return reverse('home')

    