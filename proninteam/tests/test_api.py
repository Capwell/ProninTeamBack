from django.urls import reverse
from offers.models import Offer
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase


class TestRequest(APITestCase):
    VALID_OFFER_DATA = {
        'name': 'name',
        'communicate': 'communicate',
        'is_agreed': True,
        'message': 'message' * 10
    }
    VALID_CASE_DATA = {
        'title': 'a' * 1,
        'text': 'a' * 1,
        'slug': 'a' * 1,
        'hex_color': '#' + '0' * 6
    }
    URLS = {
        'offers': reverse('api:offers:offers-list'),
        'users': reverse('api:users:users-list'),
        'cases': reverse('api:cases:cases-list'),
    }

    @parameterized.expand([
        (URLS['offers'],
         status.HTTP_405_METHOD_NOT_ALLOWED),
        (URLS['users'],
         status.HTTP_200_OK),
        (URLS['cases'],
         status.HTTP_200_OK),
    ])
    def test_response_codes(self, endpoint, expected_status_code):
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, expected_status_code)

    @parameterized.expand([
        ('name', '1' * 1,
         'Слишком короткое значение для поля "name"'),
        ('name', '1' * 21,
         'Слишком длинное значение для поля "name"'),
        ('communicate', '1' * 1,
         'Слишком короткое значение для поля "communicate"'),
        ('communicate', '1' * 21,
         'Слишком длинное значение для поля "communicate"'),
        ('is_agreed', False,
         'Некорректное значение для поля "is_agreed"'),
        ('is_agreed', '',
         'Некорректное значение для поля "is_agreed"'),
        ('is_agreed', 'false',
         'Некорректное значение для поля "is_agreed"'),
        ('is_agreed', '',
         'Некорректное значение для поля "is_agreed"'),
        ('message', '1' * 1,
         'Слишком короткое значение для поля "message"'),
    ])
    def test_not_creating_offer(self, key, not_valid_value, exception):
        not_valid_data = self.VALID_OFFER_DATA.copy()
        not_valid_data[key] = not_valid_value
        offers_count = Offer.objects.count()
        self.client.post(self.URLS['offers'], not_valid_data)
        self.assertEqual(offers_count, Offer.objects.count(), exception)

    def test_creating_offer(self):
        offers_count = Offer.objects.count()
        self.client.post(self.URLS['offers'], self.VALID_OFFER_DATA)
        self.assertEqual(offers_count + 1, Offer.objects.count())
