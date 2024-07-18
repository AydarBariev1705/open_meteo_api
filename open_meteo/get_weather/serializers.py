from rest_framework import serializers
from .models import City


class CitySerializer(serializers.ModelSerializer):
    """Сериализатор модели города"""
    class Meta:
        model = City
        fields = (
            'pk',
            'name',
            'views',

        )
