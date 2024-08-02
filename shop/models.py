from django.db import models
from django.conf import settings
# Create your models here.

class Coffee(models.Model):
        name=models.CharField(max_length=50)  
        description=models.TextField()  
        price = models.DecimalField(max_digits=5, decimal_places=2)
        image = models.ImageField(upload_to='images/menu/', null=True, blank=True)   


class Order(models.Model):
    # Field for image, optional (can be a URL or a file)
    image = models.ImageField(upload_to='order_images/', blank=True, null=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    customer = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
