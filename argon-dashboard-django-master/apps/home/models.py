
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# raw material suppliers
# class RawMaterialSuppliers(models.Model):
#     raw_materail_supplier = models.CharField(max_lenght = 30)

class SalesValue(models.Model):
    month = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.month} - {self.value}"
    
class TotalOrders(models.Model):
    month = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.month} - {self.value}"
    
class PurchaseList(models.Model):
    item = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return f"{self.item} - {self.date} - {self.quantity} - {self.price}"

class SoldProducts(models.Model):
    product = models.CharField(max_length=255)
    price = models.IntegerField()
    
    def __str__(self):
        return f"{self.product} - {self.price}"
