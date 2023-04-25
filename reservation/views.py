from django.shortcuts import render
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, viewsets
from .models import Menu, Booking
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import response

# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return response({"message":"This view is protected"})
#
def index(request):
    return render(request, 'index.html', {})

class MenuItemview(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveDestroyAPIView, generics.DestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer