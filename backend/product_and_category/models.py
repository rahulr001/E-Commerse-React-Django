from django.db import models
# from inventory.models import Inventory

# Create your models here.


class Category(models.Model):
    Category = models.CharField(max_length=20, default=None)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return f" {self.Category}"
    
    class Meta:
        db_table = 'Category'
        verbose_name_plural = 'Category'

class Product(models.Model):
    ProductName = models.CharField(max_length=20)
    Price = models.DecimalField(max_digits=7,decimal_places=2)
    Category = models.ForeignKey(Category, on_delete=models.PROTECT)
    ImageURL = models.URLField(max_length=200,default=None)
    ProductStock = models.PositiveIntegerField(default=None)
    UOM = models.CharField(max_length=10,default=None)
    Units = models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return f"{self.ProductName}"

    class Meta:
        db_table = 'Product'
        verbose_name_plural = 'Product'
