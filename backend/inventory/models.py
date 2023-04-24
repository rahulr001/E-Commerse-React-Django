from django.db import models
from product_and_category.models import Category,Product


# Create your models here.
class Inventory(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.PROTECT)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Category = models.ForeignKey(Category, on_delete=models.PROTECT)
    Quantity = models.IntegerField()
    Unit=models.CharField(max_length=10)
    Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Product}"
    
    class Meta:
        db_table = 'Inventory'
        verbose_name_plural = 'Inventory'
