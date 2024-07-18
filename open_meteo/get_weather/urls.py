from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import weather_view, CityViewSet

app_name = 'get_weather'
routers = DefaultRouter()
routers.register('', CityViewSet)
urlpatterns = [
    path('', weather_view, name='weather'),
    path('api/', include(routers.urls)),
]
