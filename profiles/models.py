from django.db import models


# Create your models here.
class Profile(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)