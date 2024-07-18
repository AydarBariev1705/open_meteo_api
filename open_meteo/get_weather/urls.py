from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from .views import weather_view, CityViewSet
from django.conf.urls.static import static
app_name = 'get_weather'
routers = DefaultRouter()
routers.register('', CityViewSet)
urlpatterns = [
    path('', weather_view, name='weather'),
    path('api/', include(routers.urls)),
]
urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
urlpatterns.extend(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )

