from typing import Any
from django.db import models

# Create your models here.
class Listing(models.Model):
    title= models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField()
    def __str__(self):
       return  self.title
    #def __init__(self):
     #   return self.price