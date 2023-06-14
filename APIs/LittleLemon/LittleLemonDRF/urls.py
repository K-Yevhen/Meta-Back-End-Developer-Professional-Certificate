# # urlpatterns = [
# #     path('menu-items', views.MenuItemsView.as_view()),
# #     path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
# #     path('category', views.CategoriesView.as_view()),
# #     path('menu-items', views.MenuItemsView.as_view()),
# #     path('ratings', views.RatingsView.as_view()),
# # ]
#
from django.urls import path
from . import views

urlpatterns = [
    path("menu-items", views.MenuItemsView.as_view()),
    path("categories", views.CategoriesView.as_view()),
    path("menu-items/<int:pk>", views.MenuItemDetailView.as_view()),
    path("groups/manager/users", views.ManagersListView.as_view()),
    path("groups/manager/users/<int:pk>", views.ManagerRemoveView.as_view()),
    path("groups/delivery-crew/users", views.DeliveryCrewListView.as_view()),
    path("groups/delivery-crew/users/<int:pk>", views.DeliveryCrewRemoveView.as_view()),
    path("cart/menu-items", views.CartItemsView.as_view()),
    path("orders", views.OrdersListCreateView.as_view()),
    path("orders/<int:pk>", views.OrderDetailView.as_view()),
]