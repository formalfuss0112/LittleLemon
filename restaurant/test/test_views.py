from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        # Create a token for the user
        self.token = Token.objects.create(user=self.user)

        # Instantiate APIClient
        self.client = APIClient()

        # Authenticate the client
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create some menu items for testing
        self.item1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = MenuItem.objects.create(title="Cake", price=150, inventory=50)

    def test_get_all_menu_items(self):
        # Send GET request with authentication
        response = self.client.get(reverse('menu-items'))
        
        # Check if response status is 200 OK
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
