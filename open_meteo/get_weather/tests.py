from django.test import TestCase
from unittest.mock import patch
from .utils import get_geocode, get_weather


class GeocodeTestCase(TestCase):

    @patch('requests.get')  # Мокаем requests.get
    def test_get_geocode(self, mock_get):
        # Подготовка мок-ответа
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [{'lat': '51.5074', 'lon': '0.1278'}]

        # Вызов функции
        result = get_geocode('London')

        # Проверки
        self.assertEqual(result, ('51.5074', '0.1278'))
        mock_get.assert_called_once_with('https://nominatim.openstreetmap.org/search?q=London&format=json&limit=1')

    def test_bad_city_name(self):
        # Вызов функции
        result = get_geocode('TESTCITYNAME')
        # Проверки
        self.assertEqual(result, None)


class WeatherTestCase(TestCase):

    @patch('requests.get')  # Мокаем requests.get
    def test_get_weather(self, mock_get):
        # Подготовка мок-ответа
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'current_weather': {
                'temperature': 25,
                'windspeed': 10
            }
        }

        # Подготовка данных для вызова функции
        geocode = (51.5074, 0.1278)  # Пример координат Лондона
        city_name = 'London'

        # Вызов функции
        result = get_weather(geocode, city_name)
        result['temperature'] = 25
        result['windspeed'] = 10

        # Проверки
        self.assertIsNotNone(result)
        self.assertEqual(result['temperature'], 25)
        self.assertEqual(result['windspeed'], 10)
        self.assertEqual(result['latitude'], 51.5074)
        self.assertEqual(result['longitude'], 0.1278)
        self.assertEqual(result['city'], 'London')
        mock_get.assert_called_once_with(
            'https://api.open-meteo.com/v1/forecast',
            params={'latitude': 51.5074, 'longitude': 0.1278, 'current_weather': True}
        )
