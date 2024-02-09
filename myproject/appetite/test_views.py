# Import necessary modules
from django.test import TestCase, Client
from django.urls import reverse
from .models import Shoe

class ShoeListViewTests(TestCase):
    def setUp(self):
        # Create sample shoes for testing
        self.shoe1 = Shoe.objects.create(type='sneakers', brand='Nike', description='Sample description 1', price=99.99)
        self.shoe2 = Shoe.objects.create(type='boots', brand='Timberland', description='Sample description 2', price=149.99)

    def test_shoe_list_view(self):
        # Test if the shoe list view returns status code 200
        response = self.client.get(reverse('shoe-list-create'))
        self.assertEqual(response.status_code, 200)

    def test_shoe_list_view_with_filter(self):
        # Test if the shoe list view filters correctly based on type
        response = self.client.get(reverse('shoe-list-create') + '?type=sneakers')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.shoe1.brand)
        self.assertNotContains(response, self.shoe2.brand)

    def test_shoe_list_view_with_search(self):
        # Test if the shoe list view filters correctly based on brand
        response = self.client.get(reverse('shoe-list-create') + '?brand=Nike')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.shoe1.brand)
        self.assertNotContains(response, self.shoe2.brand)

class CreateShoeViewTests(TestCase):
    def test_create_shoe_view_get(self):
        # Test if the create shoe view returns status code 200 for GET request
        response = self.client.get(reverse('create_shoe'))
        self.assertEqual(response.status_code, 200)

    # You can add more tests here for POST request handling, form validation, etc.

