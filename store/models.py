from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)



class Customer(models.Model):
    frist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
