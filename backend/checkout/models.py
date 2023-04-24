from django.db import models
from cart.models import Cart
from datetime import datetime,timedelta
# Create your models here.

class Checkout(models.Model):
    Cart = models.ManyToManyField(Cart)
    CustomerName = models.CharField(max_length=30)
    MobileNumber = models.BigIntegerField()
    DeliveryAddress = models.TextField(max_length=60)
    PaymentOptions = (
        ('Debit Card','Debit Card'),
        ('Credit Card','Credit Card'),
        ('UPI','UPI')
    )
    PaymentMode = models.CharField(choices=PaymentOptions,max_length=20)
    DeliveryDate = models.DateField(default=datetime.now().date() + timedelta(days=3))


    class Meta:
        db_table = 'Checkout'
        verbose_name_plural = 'Checkout'

    def __str__(self):
        return f"{self.CustomerName}"