from django.contrib import admin
from .models import Sensor, Measurement

# Register your models here.

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_list_display = ['id', 'title', 'description']
    list_filter = ['id', 'title']

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'sensor', 'temperature', 'date_measurement']
    list_filter = ['id', 'date_measurement']