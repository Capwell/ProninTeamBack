from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Request


class TestRequest(APITestCase):
    def test_creating_response_code(self):
        data = {
            "name": "name",
            "communicate": "communicate",
            "is_agreed": "True",
            "message": "message" * 10
        }
        url = reverse("api:requests-list")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_is_creating(self):
        data = {
            "name": "nametest",
            "communicate": "communicate",
            "is_agreed": "True",
            "message": "message" * 10
        }
        requests_count = Request.objects.count()
        url = reverse("api:requests-list")
        self.client.post(url, data)
        new_requests_count = Request.objects.count()
        self.assertTrue(requests_count < new_requests_count)
