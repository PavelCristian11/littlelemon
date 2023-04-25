from django.shortcuts import render
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, viewsets
from .models import Menu, Booking

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class MenuItemview(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveDestroyAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer