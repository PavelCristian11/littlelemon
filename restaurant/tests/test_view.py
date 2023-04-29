from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=80.0, inventory=100)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "IceCream : 80.0")