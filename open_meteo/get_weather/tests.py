from django.test import TestCase, Client, RequestFactory
from unittest.mock import patch
from django.urls import reverse
from .utils import get_geocode, get_weather
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .models import City
from .views import CityViewSet
from .serializers import CitySerializer


# class GeocodeTestCase(TestCase):
#
#     @patch('requests.get')
#     def test_get_geocode(self, mock_get):
#         mock_response = mock_get.return_value
#         mock_response.status_code = 200
#         mock_response.json.return_value = [{'lat': '51.5074', 'lon': '0.1278'}]
#
#         result = get_geocode('London')
#
#         self.assertEqual(result, ('51.5074', '0.1278'))
#         mock_get.assert_called_once_with('https://nominatim.openstreetmap.org/search?q=London&format=json&limit=1')
#
#     def test_bad_city_name(self):
#
#         result = get_geocode('TESTCITYNAME')
#
#         self.assertEqual(result, None)
#
#
# class WeatherTestCase(TestCase):
#
#     @patch('requests.get')
#     def test_get_weather(self, mock_get):
#         mock_response = mock_get.return_value
#         mock_response.status_code = 200
#         mock_response.json.return_value = {
#             'current_weather': {
#                 'temperature': 25,
#                 'windspeed': 10
#             }
#         }
#
#         geocode = (51.5074, 0.1278)  # Пример координат Лондона
#         city_name = 'London'
#
#         # Вызов функции
#         result = get_weather(geocode, city_name)
#         result['temperature'] = 25
#         result['windspeed'] = 10
#
#         # Проверки
#         self.assertIsNotNone(result)
#         self.assertEqual(result['temperature'], 25)
#         self.assertEqual(result['windspeed'], 10)
#         self.assertEqual(result['latitude'], 51.5074)
#         self.assertEqual(result['longitude'], 0.1278)
#         self.assertEqual(result['city'], 'London')
#         mock_get.assert_called_once_with(
#             'https://api.open-meteo.com/v1/forecast',
#             params={'latitude': 51.5074, 'longitude': 0.1278, 'current_weather': True}
#         )
#
#
# class WeatherViewTestCase(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#
#     def test_weather_view_post_valid_form(self):
#         url = reverse('get_weather:weather')
#         data = {'city': 'Moscow'}
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('form', response.context)
#
#     def test_weather_view_city_not_found(self):
#         url = reverse('get_weather:weather')
#         data = {'city': 'TESTCITYNAME'}
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('form', response.context)
#         self.assertIn('error', response.context)
#
#     def test_weather_view_last_viewed_city_in_session(self):
#         url = reverse('get_weather:weather')
#         data = {'city': 'Paris'}
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('last_viewed_city', self.client.session)
#         self.assertEqual(self.client.session['last_viewed_city']['city'], 'Paris')
#
#     def test_weather_view_no_last_viewed_city_in_session(self):
#         url = reverse('get_weather:weather')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertNotIn('last_viewed_city', self.client.session)


class CityViewSetTestCase(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CityViewSet.as_view({'get': 'list'})
        self.url = '/api/'

    def test_list_cities(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

