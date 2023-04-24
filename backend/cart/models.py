from django.db import models
from product_and_category.models import Product
# Create your models here.

class Cart(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.PROTECT)
    CartQuantity = models.PositiveIntegerField(default=1)
    CartPrice = models.IntegerField(null=True)
    PaymentStatus = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.Product.ProductName}"

    class Meta:
        db_table = 'Cart'
        verbose_name_plural = 'Cart'