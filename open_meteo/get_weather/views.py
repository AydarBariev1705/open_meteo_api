from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CitySerializer

from .models import City
from django.http import HttpRequest
from django.shortcuts import render

from .forms import CityForm
from .utils import get_weather, get_geocode, add_view


def weather_view(request: HttpRequest):
    """Функция для получения погоды """
    form = CityForm()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city'].title()
            geocode = get_geocode(city)
            if not geocode:
                context = {
                    'form': form,
                    'error': f'Город: {city} не найден!',
                }
                return render(
                    request,
                    template_name='get_weather/index.html',
                    context=context
                )
            weather_data = get_weather(geocode, city)
            if weather_data:
                add_view(city)
                request.session['last_viewed_city'] = {
                    'geocode': geocode,
                    'city': city
                }

    last_viewed_city = request.session.get('last_viewed_city')
    if last_viewed_city:
        weather_data = get_weather(last_viewed_city['geocode'], last_viewed_city['city'])
    else:
        weather_data = None
    context = {
        'form': form,
        'weather_data': weather_data,
    }
    return render(request,
                  template_name='get_weather/index.html',
                  context=context
                  )


class CityViewSet(ModelViewSet):
    """Апи для отображения истории запросов """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = [
        'name',
        'views',
    ]
    filterset_fields = [
        'name',
        'views',
    ]
    ordering_fields = [
        'name',
        'views',
    ]
