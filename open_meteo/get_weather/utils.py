from .models import City
import requests


def add_view(city_name: str):
    """Функция для записи города в БД и для увеличения просмотров"""
    city, created = City.objects.get_or_create(
        name=city_name,
    )
    city.views += 1
    city.save()


def get_weather(geocode: tuple, city_name: str):
    """Функция для получения погоды по широте и долготе"""
    latitude = geocode[0]
    longitude = geocode[1]
    current_url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current_weather': True
    }
    response = requests.get(current_url, params=params)
    current_data = response.json()

    if 'current_weather' in current_data:
        weather_info = {
            'temperature': current_data['current_weather']['temperature'],
            'latitude': latitude,
            'longitude': longitude,
            'city': city_name,
            'windspeed': current_data['current_weather']['windspeed'],

        }

        return weather_info
    else:
        return None


def get_geocode(city_name: str):
    """Функция для получения широты и долготы по названию города"""
    limit = 1
    geocode_url = f'https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit={limit}'
    response = requests.get(geocode_url)
    if response.status_code == 200:
        geocode_data = response.json()
        if geocode_data:
            latitude = geocode_data[0]['lat']
            longitude = geocode_data[0]['lon']
            result = (latitude, longitude)
            print(result)
            return result
