from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class DetailTestCase(APITestCase):

    login = reverse('rest_framework:login')
    logout = reverse('rest_framework:logout')
    list = reverse('all_article')

    def test_login(self):
        response = self.client.get(self.login)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        response = self.client.get(self.logout)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list(self):
        response = self.client.get(self.list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

