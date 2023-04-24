from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here


class AuthUser(AbstractUser):
    CreatedAt = models.DateTimeField(auto_now_add=True,  blank=False, null=False)
    UpdatedAt = models.DateTimeField(auto_now=True, blank=False, null=False)

    class Meta:
        db_table = 'AuthUser'
        verbose_name_plural = 'AuthUser'
