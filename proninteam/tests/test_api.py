from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Offer


class TestRequest(APITestCase):
    DATA = {
        'name': 'name',
        'communicate': 'communicate',
        'is_agreed': 'True',
        'message': 'message' * 10
    }
    URL = reverse('api:requests-list')

    def test_creating_response_code(self):
        response = self.client.post(self.URL, self.DATA)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_is_creating(self):
        requests_count = Offer.objects.count()
        self.client.post(self.URL, self.DATA)
        new_requests_count = Offer.objects.count()
        self.assertTrue(requests_count + 1 == new_requests_count)
