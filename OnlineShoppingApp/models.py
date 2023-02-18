from django.db import models

# Create your models here.
class Customers (models.Model):
    name = models.CharField(max_length=50)
    contact_add = models.PositiveIntegerField()
    address = models.TextField()


class ShoppingOrder (models.Model):
    customer_ID = models.ForeignKey (Customers,on_delete=models.CASCADE)
    date = models.DateField()

class Categories (models.Model):
    category_name = models.CharField (max_length=50)
    category_type = models.CharField(max_length=50)

class Products (models.Model):
    category_ID = models.ForeignKey(Categories,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)

class Payment (models.Model):
    category_ID = models.ForeignKey(Categories,on_delete=models.CASCADE)
    date = models.DateField()

class TransactionReports (models.Model):
    customer_ID = models.ForeignKey(Customers,on_delete=models.CASCADE)
    order_ID = models.ForeignKey(ShoppingOrder,on_delete=models.CASCADE)
    product_ID = models.ForeignKey(Products,on_delete=models.CASCADE)
    payment_ID = models.ForeignKey(Payment,on_delete=models.CASCADE)

class Deliveries (models.Model):
    customer_ID = models.ForeignKey(Customers,on_delete=models.CASCADE)
    date = models.DateField()

class Seller (models.Model):
    product_ID = models.ForeignKey(Products,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)