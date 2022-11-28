from django.urls import reverse
from rest_framework.test import APITestCase

from api.models import Request


class TestRequest(APITestCase):
    def test_creating_response_code(self):
        data = {
            "name": "name",
            "communicate": "communicate",
            "is_agreed": "True",
            "message": ("messagemessage"
                        "messagemessage"
                        "messagemessage"
                        "messagemessage")
        }
        url = reverse("api:requests-list")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_creating_request(self):
        data = {
            "name": "nametest",
            "communicate": "communicate",
            "is_agreed": "True",
            "message": ("messagemessage"
                        "messagemessage"
                        "messagemessage"
                        "messagemessage")
        }
        url = reverse("api:requests-list")
        self.client.post(url, data)
        self.assertTrue(Request.objects.filter(**data).exists())
