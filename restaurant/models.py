from django.db import models

# Create your models here.

class Booking(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    no_of_guests = models.IntegerField(null=False)
    booking_date = models.DateField(null=False)
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.first_name 
    
class Menu(models.Model):
    title = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    inventory = models.IntegerField()
    #permission_classes = [IsA]

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
