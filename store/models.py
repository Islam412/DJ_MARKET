from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)





MEMBER_BRONZE = 'Bronze'
MEMBER_Sliver = 'Sliver'
MEMBER_Gold = 'Gold'

MEMBER_CHOICES = [
    (MEMBER_BRONZE,'Bronze'),
    ('Sliver','Sliver'),
    ('Gold','Gold'),
]

class Customer(models.Model):
    frist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=100,choices=MEMBER_CHOICES,default=MEMBER_BRONZE)




PAYMENT_STATUS_PENDING = 'Pending'
PAYMENT_STATUS_COMPLETE = 'Complete'
PAYMENT_STATUS_FAILED = 'Failed'

PAYMENT_STATUS_CHOICES = [
    (PAYMENT_STATUS_PENDING, 'Pending'),
    (PAYMENT_STATUS_COMPLETE, 'Complete'),
    (PAYMENT_STATUS_FAILED, 'Failed'),
]

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING)