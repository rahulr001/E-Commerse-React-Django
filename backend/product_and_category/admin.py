from django.contrib import admin
from .models import * 
# Register your models here.

models = [Category,Product]
admin.site.register(models)