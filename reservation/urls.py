from django.urls import path, include
from reservation import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemview.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]