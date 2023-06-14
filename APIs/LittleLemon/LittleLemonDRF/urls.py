from django.urls import path
# from .views import MenuItemsView, MenuItemDetail, UserGroupManagement, RemoveUserFromManagerGroup, DeliveryCrewManagerGroup, RemoveUserFromDeliveryCrewGroup, CartView, RemoveCartItem, OrderView, OrderDetail
from . import views
# urlpatterns = [
#     path('menu-items', views.MenuItemsView.as_view()),
#     path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
#     path('category', views.CategoriesView.as_view()),
#     path('menu-items', views.MenuItemsView.as_view()),
#     path('ratings', views.RatingsView.as_view()),
# ]
#
urlpatterns = [
    path('menu-items/', views.MenuItemsView),
    path('menu-items/<int:id>', views.MenuItemDetail),
    path('groups/manager/users', views.UserGroupManagement),
    path('groups/manager/users/<int:id>', views.RemoveUserFromManagerGroup),
    path('groups/delivery-crew/users', views.DeliveryCrewManagerGroup),
    path('groups/delivery-crew/users/<int:id>', views.RemoveUserFromDeliveryCrewGroup),
    path('cart/menu-items', views.CartView),
    path('cart/menu-items/<int:id>', views.RemoveCartItem),
    path('orders/', views.OrderView),
    path('orders/<int:id>', views.OrderDetail),
]
