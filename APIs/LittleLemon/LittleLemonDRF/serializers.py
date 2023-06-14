from rest_framework import serializers
# from .models import MenuItem, Category
# from .models import Rating
# from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from .models import Category, MenuItem, Cart, Order, OrderItem


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'title']
#
#
# class MenuItemSerializer(serializers.ModelSerializer):
#     category_id = serializers.IntegerField(write_only=True)
#     category = CategorySerializer(read_only=True)
#
#     class Meta:
#         model = MenuItem
#         fields = [
#             'id', 'title', 'price', 'inventory', 'category', 'category_id'
#         ]

# class RatingSerializer (serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(
#     queryset=User.objects.all(),
#     default=serializers.CurrentUserDefault()
#     )
#
#     class Meta:
#         model = Rating
#         fields = ['user', 'menuitem_id', 'rating']
#
#     validators = [
#         UniqueTogetherValidator(
#             queryset=Rating.objects.all(),
#             fields=['user', 'menuitem_id']
#         )
#     ]
#
#     extra_kwargs = {
#         'rating': {
#             'max_value': 5,
#             'min_value': 0
#         }
#     }
#
#


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    menuitem = MenuItemSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    order = UserSerializer(read_only=True)
    menuitem = MenuItemSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    delivery_crew = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
