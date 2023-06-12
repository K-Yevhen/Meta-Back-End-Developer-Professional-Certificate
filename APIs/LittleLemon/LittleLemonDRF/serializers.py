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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = [
            'id', 'title', 'price', 'featured', 'category', 'category_id'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class CartItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields = ['id', 'user', 'menuitem', 'quantity', 'unit_price', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'menuitem', 'quantity', 'unit_price', 'price']
        