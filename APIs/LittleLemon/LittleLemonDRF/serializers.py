# from rest_framework import serializers
# from .models import MenuItem, Category
# from .models import Rating
# from rest_framework.validators import UniqueTogetherValidator
# from django.contrib.auth.models import User
# from .models import Category, MenuItem, Cart, Order, OrderItem


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
from rest_framework import serializers
from .models import MenuItem, Category, Cart, Order, OrderItem
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # for GET requests
    category_id = serializers.IntegerField(
        write_only=True)  # for POST, PUT, PATCH requests, it won't appear in GET requests

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category', 'category_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class CartItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields = ('id', 'user', 'menuitem', 'quantity', 'unit_price', 'price')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'menuitem', 'quantity', 'unit_price', 'price']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'delivery_crew', 'status', 'order_items', 'total', 'date')


class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('order_items',)
