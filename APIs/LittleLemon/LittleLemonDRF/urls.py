from django.urls import path
from . import views

# urlpatterns = [
#     path('menu-items', views.MenuItemsView.as_view()),
#     path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
# ]

urlpatterns = [
    # path('category', views.CategoriesView.as_view()),
    # path('menu-items', views.MenuItemsView.as_view()),
    path('ratings', views.RatingsView.as_view()),
]
