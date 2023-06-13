# from django.shortcuts import render
# from .models import MenuItem, Category
# from .serializers import MenuItemSerializer, CategorySerializer
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from .models import Rating
# from .serializers import RatingSerializer

# Create your views here.

# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializers

# class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializers


# class CategoriesView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer
#     ordering_fields = ['price', 'inventory']
#     filterset_fields = ['price', 'inventory']
#     search_fields = ['title']

# class RatingsView(generics.ListCreateAPIView):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
#
#     def get_permissions(self):
#         if (self.request.method == 'GET'):
#             return []
#
#         return [IsAuthenticated()]


from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import CategorySerializer, MenuItemSerializer, \
    CartItemSerializer, UserSerializer, OrderItemSerializer, OrderSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django.contrib.auth.models import User, Group

@csrf_exempt
@throttle_classes([AnonRateThrottle, UserRateThrottle])
class MenuItemsView(generics.ListCreateAPIView):
    def get(self, request):
        queryset = MenuItem.objects.all()
        serializer_class = MenuItemSerializer(queryset, many=True)
        filter_backends = [OrderingFilter, SearchFilter]
        ordering_fields = ['title', 'price', 'category']
        filterset_fields = ['title', 'price', 'category']
        search_fields = ['category']
        try:
            if request.user.has_perm('LittleLemonAPI.view_menuitem'):
                return Response(serializer_class.data, status=status.HTTP_200_OK)
        except:
            return Response("Not authorized to view this page", status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        try:
            if request.user.groups.filter(name="Manager"):
                data = MenuItemSerializer(data=request.data)
                if data.is_valid():
                    data.save()
                    return Response(data.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(data.errors, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response("Not authorized...", status=status.HTTP_403_FORBIDDEN)

