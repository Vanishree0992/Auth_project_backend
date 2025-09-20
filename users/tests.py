from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class AuthTests(APITestCase):

    def test_register_user(self):
        url = reverse('register')  # make sure your urls.py has name='register'
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "Test@1234",
            "password2": "Test@1234"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_login_user(self):
        # Create user first
        User.objects.create_user(username="testuser", password="Test@1234")
        url = reverse('login')  # make sure your urls.py has name='login'
        data = {
            "username": "testuser",
            "password": "Test@1234"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
