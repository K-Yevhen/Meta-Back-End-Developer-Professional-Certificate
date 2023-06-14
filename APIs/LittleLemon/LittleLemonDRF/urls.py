from django.urls import path
from . import views
# # urlpatterns = [
# #     path('menu-items', views.MenuItemsView.as_view()),
# #     path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
# #     path('category', views.CategoriesView.as_view()),
# #     path('menu-items', views.MenuItemsView.as_view()),
# #     path('ratings', views.RatingsView.as_view()),
# # ]
#
urlpatterns = [
    path("menu-items", views.MenuItemsView),
    path("categories", views.CategoriesView),
    path("menu-items/<int:pk>", views.MenuItemDetailView),
    path("groups/manager/users", views.ManagersListView),
    path("groups/manager/users/<int:pk>", views.ManagerRemoveView),
    path("groups/delivery-crew/users", views.DeliveryCrewListView),
    path("groups/delivery-crew/users/<int:pk>", views.DeliveryCrewRemoveView),
    path("cart/menu-items", views.CartItemsView),
    path("orders", views.OrdersListCreateView),
    path("orders/<int:pk>", views.OrderDetailView),
]
