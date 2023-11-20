from django.db import models


class Promotions(models.Model):
    description = models.CharField(max_length=255)
    discound = models.FloatField( )


class Collection(models.Model):
    title = models.CharField(max_length=255)
    fratured_product = models.ForeignKey('Product',related_name='product1', on_delete=models.SET_NULL,null=True)

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(max_length=10000)
    unit_price = models.DecimalField(max_digits=6 , decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotions)





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
    customer_address = models.CharField(max_length=255)

    class Meta:
        db_table = 'store_customers'
        indexes = [
            models.Index(fields=['last_name','frist_name'])
        ]




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


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)

class Address(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    Customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    Cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()