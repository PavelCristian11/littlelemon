from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255, null=False)
    no_of_guests = models.IntegerField(null=False)
    booking_date = models.DateTimeField(null=False)

    def __str__(self):
        return self.name 
    
class Menu(models.Model):
    title = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    inventory = models.IntegerField()
    #permission_classes = [IsA]

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
