from django.urls import path
from .views import MenuItemsView, MenuItemDetail, UserGroupManagement, RemoveUserFromManagerGroup, DeliveryCrewManagerGroup, RemoveUserFromDeliveryCrewGroup, CartView, RemoveCartItem, OrderView, OrderDetail

# urlpatterns = [
#     path('menu-items', views.MenuItemsView.as_view()),
#     path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
#     path('category', views.CategoriesView.as_view()),
#     path('menu-items', views.MenuItemsView.as_view()),
#     path('ratings', views.RatingsView.as_view()),
# ]
#
urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:id>', views.MenuItemDetail.as_view()),
    path('groups/manager/users', UserGroupManagement.as_view()),
    path('groups/manager/users/<int:id>', RemoveUserFromManagerGroup.as_view()),
    path('groups/delivery-crew/users', DeliveryCrewManagerGroup.as_view()),
    path('groups/delivery-crew/users/<int:id>', RemoveUserFromDeliveryCrewGroup.as_view()),
    path('cart/menu-items', CartView.as_view()),
    path('cart/menu-items/<int:id>', RemoveCartItem.as_view()),
    path('orders/', OrderView.as_view()),
    path('orders/<int:id>', OrderDetail.as_view()),
]
