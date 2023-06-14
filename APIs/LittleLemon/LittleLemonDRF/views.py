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
from .serializers import CategorySerializer, MenuItemSerializer, CartItemSerializer, UserSerializer, OrderItemSerializer, OrderSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView


@throttle_classes([AnonRateThrottle, UserRateThrottle])
@api_view(["GET", "POST"])
class MenuItemsView(APIView):
    def get(self, request):
        queryset = MenuItem.objects.all()
        serializer_class = MenuItemSerializer(queryset, many=True)
        filter_backends = [OrderingFilter, SearchFilter]
        ordering_fields = ['title', 'price', 'category']
        filterset_fields = ['title', 'price', 'category']
        search_fields = ['category']
        if request.user.has_perm('LittleLemonAPI.view_menuitem'):
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        return Response("Not authorized to view this page", status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        if request.user.groups.filter(name="Manager"):
            data = MenuItemSerializer(data=request.data)
            if data.is_valid():
                data.save()
                return Response(data.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data.errors, status=status.HTTP_403_FORBIDDEN)
        return Response("Not authorized...", status=status.HTTP_403_FORBIDDEN)



@throttle_classes([AnonRateThrottle, UserRateThrottle])
@api_view(["GET", "PUT", "DELETE"])
class MenuItemDetail(APIView):
    def get_object(self, id):
        try:
            return MenuItem.objects.get(id=id)
        except MenuItem.DoesNotExist:
            pass

    def get(self, request, id):
        serializer_class = MenuItemSerializer(self.get_object(id))
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            serializer_class = self.get_object(id)
            data = MenuItemSerializer(serializer_class, data=request.data)
            if request.user.groups.filter(name="Manager"):
                if data.is_valid():
                    data.save()
                    return Response(data.data, status=status.HTTP_201_CREATED)
        except:
            return Response("Not authorised to make changes", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, id):
        try:
            serializer_class = self.get_object(id)
            if request.user.groups.filter(name="Manager"):
                serializer_class.delete()
                return Response("Deleted Successfully", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Not authorised to remove item", status=status.HTTP_403_FORBIDDEN)



@throttle_classes([AnonRateThrottle, UserRateThrottle])
@api_view(["GET", "POST"])
class UserGroupManagement(APIView):
    def get(self, request):
        try:
            users = User.objects.filter(groups__name="Manager")
            users_data = UserSerializer(users, many=True)
            if request.user.groups.filter(name="Manager"):
                return Response(users_data.data)
        except:
            return Response("Not authorized to view this page", status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        try:
            if request.user.groups.filter(name="Manager"):
                serializer_class = UserSerializer(data=request.data)
                if serializer_class.is_valid():
                    user = serializer_class.save()
                    manager_group = Group.objects.get(name='Manager')
                    manager_group.user_set.add(user)
                    return Response(serializer_class.data, status=status.HTTP_201_CREATED)
                return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Not authorized...", status=status.HTTP_401_UNAUTHORIZED)



@throttle_classes([AnonRateThrottle, UserRateThrottle])
@api_view(["DELETE"])
class RemoveUserFromManagerGroup(APIView):
    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        group = Group.objects.get(name='Manager')
        if request.user.groups.filter(name="Manager"):
            if group in user.groups.all():
                user.groups.remove(group)
                return Response("User removed successfully!", status=status.HTTP_200_OK)
            else:
                return Response({'error': 'User is not a member of the manager group'}, status=status.HTTP_400_BAD_REQUEST)
        return Response("Not authorized", status=status.HTTP_401_UNAUTHORIZED)



@throttle_classes([AnonRateThrottle, UserRateThrottle])
@api_view(["GET", "POST"])
class DeliveryCrewManagerGroup(APIView):
    def get(self, request):
        users = User.objects.filter(groups__name="Delivery crew")
        serializer_class = UserSerializer(users, many=True)
        if request.user.groups.filter(name="Manager"):
            return Response(serializer_class.data)
        return Response("Not authorized to view this page", status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, format=None):
        if request.user.groups.filter(name="Manager"):
            serializer_class = UserSerializer(data=request.data)
            if serializer_class.is_valid():
                user = serializer_class.save()
                manager_group = Group.objects.get_or_create(name='Delivery crew')
                manager_group.user_set.add(user)
                return Response(serializer_class.data, status=status.HTTP_201_CREATED)
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Not authorized...", status=status.HTTP_401_UNAUTHORIZED)



@throttle_classes([AnonRateThrottle, UserRateThrottle])
@api_view(["DELETE"])
class RemoveUserFromDeliveryCrewGroup(APIView):
    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        group = Group.objects.get(name='Delivery crew')
        if request.user.groups.filter(name="Manager"):
            if group in user.groups.all():
                user.groups.remove(group)
                return Response("User removed successfully!", status=status.HTTP_200_OK)
            else:
                return Response({'error': 'User is not a member of the manager group'}, status=status.HTTP_400_BAD_REQUEST)
        return Response("Not authorized", status=status.HTTP_401_UNAUTHORIZED)



@throttle_classes([AnonRateThrottle, UserRateThrottle])
@api_view(["GET", "POST"])
class CartView(APIView):
    def get(self, request):
        user = request.user
        carts = Cart.objects.filter(user=user)
        serializer_class = CartItemSerializer(carts, many=True)
        if request.user.groups.filter(name="customer"):
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        return Response("Not authorized to view this page", status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        if request.user.groups.filter(name="customer"):
            serializer_class = CartItemSerializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=status.HTTP_200_OK)
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Not authorized...", status=status.HTTP_400_BAD_REQUEST)


@throttle_classes([AnonRateThrottle, UserRateThrottle])
@api_view(["DELETE"])
class RemoveCartItem(APIView):
    def get_object(self, id):
        try:
            return Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return Response("Cart object not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        if request.user.groups.filter(name="customer"):
            cart = self.get_object(id)
            if cart.user == request.user:
                cart.delete()
                return Response("Cart deleted successfully!", status=status.HTTP_404_NOT_FOUND)
            return Response("Not authorized to delete", status=status.HTTP_401_UNAUTHORIZED)
        return Response("Not authorized to remove cart!", status=status.HTTP_401_UNAUTHORIZED)



@throttle_classes([AnonRateThrottle, UserRateThrottle])
@api_view(["GET", "POST"])
class OrderView(APIView):
    def get(self, request):
        user = request.user
        orders = Order.objects.filter(user=user)
        serializer_class = OrderSerializer(orders, many=True)

        if request.user.groups.filter(name="customer"):
            return Response(serializer_class.data, status=status.HTTP_200_OK)

        elif request.user.groups.filter(name="Manager"):
            all_orders = OrderItem.objects.all()
            all_orders_serializer = OrderItemSerializer(all_orders, many=True)
            return Response(all_orders_serializer.data, status=status.HTTP_200_OK)

        elif request.user.groups.filter(name="Delivery crew"):
            orders = Order.objects.filter(delivery_crew=request.user)
            serializer_class = OrderSerializer(orders, many=True)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

        return Response("Not authorized...", status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        if request.user.group.filter(name="customer"):
            user = request.user
            cart_items = Cart.objects.filter(user=user)

            for item in cart_items:
                order_item = OrderItem.objects.create(
                order=request.user,
                menuitem=item.menuitem,
                quantity=item.quantity,
                unit_price=item.unit_price,
                price=item.price,
            )
            cart_items.delete()
            return Response({"message": "Order items created and cart items deleted successfully."}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@throttle_classes([AnonRateThrottle, UserRateThrottle])
@api_view(["GET", "PUT", "DELETE"])
class OrderDetail(APIView):
    def get_object(self, id):
        try:
            return Order.objects.get(id=id)
        except Order.DoesNotExist:
            pass

    def get(self, request, id):
        order_item = OrderSerializer(self.get_object(id))
        if request.user.groups.filter(name="customer"):
            return Response(order_item.data, status=status.HTTP_200_OK)
        else:
            return Response("Not authorized to view this page", status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, id):
        order_item = OrderSerializer(self.get_object(id))
        if request.user.groups.filter(name="customer" or "Manager"):
            serializer_class = OrderSerializer(order_item, data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=status.HTTP_201_CREATED)
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.user.groups.filter(name="Delivery crew"):
            order = OrderSerializer(order_item, data=request.data)
            if order.is_valid():
                order.save()
                return Response("Updated successfully", status=status.HTTP_201_CREATED)
            return Response(order.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Not authorized", status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, id):
        if request.user.groups.filter(name="Manager"):
            order_item = self.get_object(id)
            order_item.delete()
            return Response("Deleted successfully!", status=status.HTTP_404_NOT_FOUND)
        return Response("Not authorized to remove this order", status=status.HTTP_401_UNAUTHORIZED)
