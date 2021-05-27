from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)