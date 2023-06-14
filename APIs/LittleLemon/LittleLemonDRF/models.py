from django.db import models
from django.contrib.auth.models import User


# # Create your models here.
# class Category(models.Model):
#     slug = models.SlugField()
#     title = models.CharField(max_length=255)
#     fields = ['slug', 'title']
#
#     def __str__(self) -> str:
#         return self.title
#
#
# class MenuItem(models.Model):
#     title = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     inventory = models.SmallIntegerField()
#     category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
#
#     def __str__(self) -> str:
#         return self.title

# class Rating(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     menuitem_id = models.SmallIntegerField()
#     rating = models.SmallIntegerField()

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    def __init__(self, title):
        self.title = title

class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __init__(self, title):
        self.title = title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ['menuitem', 'user']

    def __init__(self, title, menuitem):
        self.menuitem.title = menuitem, title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="delivery_crew")
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)

    def __str__(self):
        return f"{self.user.username} -> {self.delivery_crew.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ['order', 'menuitem']

    def __str__(self):
        return f"{self.order.username} -> {self.menuitem}"
