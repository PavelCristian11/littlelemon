from django.urls import path, include
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='home'),
    path('menu-items/', views.MenuItemview.as_view(), name='menu-items'),                #api
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),  #api
    path('api-token-auth/', obtain_auth_token),
    path('reservations/', views.reservations, name="reservations"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('bookings/', views.bookings, name='bookings'),
]