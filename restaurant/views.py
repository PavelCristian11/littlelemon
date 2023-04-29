from django.shortcuts import render
from .serializers import MenuSerializer, BookingSerializer
from django.core import serializers
from rest_framework import generics, viewsets
from .models import Menu, Booking
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .forms import BookingForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
#
def index(request):
    return render(request, 'home.html', {})

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

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'reservations.html',{"bookings":booking_json})

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        print(data)
        exist = Booking.objects.filter(booking_date=data['booking_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Booking(
                first_name=data['first_name'],
                booking_date=data['booking_date'],
                reservation_slot=data['reservation_slot'],
                no_of_guests = data['no_of_guests'],
            )
            booking.save()
            return JsonResponse({
                'message': 'success'
            })
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())

    bookings = Booking.objects.all().filter(booking_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')