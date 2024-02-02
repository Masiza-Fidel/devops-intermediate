# shoes/tests/test_views.py
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Shoe

class ShoeAPITestCase(APITestCase):
    def setUp(self):
        # Create some sample shoes for testing
        Shoe.objects.create(type='sneakers', brand='Nike', description='Comfortable sneakers', price=150.00)
        Shoe.objects.create(type='boots', brand='Timberland', description='Durable boots', price=200.00)

    def test_create_shoe(self):
        url = reverse('shoe-list-create')
        data = {'type': 'casual', 'brand': 'Adidas', 'description': 'Stylish casual shoes', 'price': 120.00}
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shoe.objects.count(), 3)

    def test_list_shoes(self):
        url = reverse('shoe-list-create')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Assuming you have 2 initial shoes

    # Add more tests as needed
