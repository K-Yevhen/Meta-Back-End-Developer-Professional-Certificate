from django.urls import path
from . import views


urlpatterns = [
        path('', views.home, name="home"),
        path('about/', views.about, name="about"),
        path('book/', views.book, name="book"),
        # path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
        path('menu/', views.menu, name="menu"),
        path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
        # path('booking/', views.form_view),
]
