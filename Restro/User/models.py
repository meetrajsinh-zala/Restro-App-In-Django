from django.db import models

# Create your models here.
class User_Register(models.Model):
    Guest_name = models.CharField(max_length=100)
    Guest_email = models.CharField(max_length=100)
    Guest_number = models.CharField(max_length=10)
    Guest_password = models.CharField(max_length=10)

class User_Order(models.Model):
    Guest_name = models.CharField(max_length=100)
    Guest_email = models.CharField(max_length=100)
    Item_name = models.CharField(max_length=500)
    grand_Total = models.CharField(max_length=100)
    Payment_method = models.CharField(max_length=100)