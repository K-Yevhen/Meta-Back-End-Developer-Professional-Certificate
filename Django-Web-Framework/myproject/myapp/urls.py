from django.urls import path
from . import views


urlpatterns = [
        path('', views.home, name="home"),
        path('about/', views.about, name="about"),
        path('book/', views.book, name="book"),
        # path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
        path('menu/', views.menu, name="menu"),
        # path('booking/', views.form_view),
]
