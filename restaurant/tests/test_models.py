from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='IceCream', price=80.0, inventory=100)
        Menu.objects.create(title='Pie', price=10.0, inventory=110)

        self.serializer_data_1 = {
            'id' : 1,
            'title': 'IceCream',
            'price': '80.00',
            'inventory': 100,
        }
        self.serializer_data_2 = {
            'id' : 2,
            'title': 'Pie',
            'price': '10.00',
            'inventory': 110
        }
    
    def test_getall(self):
        items = Menu.objects.all()
        #print(MenuSerializer(items[0]).data, self.serializer_data_1)
        self.assertEqual(MenuSerializer(items[0]).data, self.serializer_data_1)
        self.assertEqual(MenuSerializer(items[1]).data, self.serializer_data_2)