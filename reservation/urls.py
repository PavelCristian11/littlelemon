from django.urls import path
from reservation import views

urlpatterns = [
    path('index/', views.index, name='index')
]