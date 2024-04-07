from django.db import models

# Create your models here.
class Admin_Details(models.Model):
    Username = models.CharField(max_length=250)
    Password = models.CharField(max_length=16)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255) # Adjust upload path as needed
    category = models.CharField(max_length=100)