from django.db import models


# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    fields = ['slug', 'title']


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
