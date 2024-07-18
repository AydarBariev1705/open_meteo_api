from django.contrib import admin
from .models import City


@admin.register(City)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'pk', 'views',
    ordering = 'pk',
