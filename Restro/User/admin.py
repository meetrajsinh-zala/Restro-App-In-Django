from django.contrib import admin
from .models import User_Register
from .models import User_Order
# Register your models here.

admin.site.register(User_Register)
admin.site.register(User_Order)