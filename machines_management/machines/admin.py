from django.contrib import admin
from .models import Machine, Sensor, SensorData


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('machine_name', 'machine_location', 'user')
    list_filter = ('user',)
    search_fields = ('machine_name', 'machine_location', 'user__username')
    ordering = ('user', 'machine_name')


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_name', 'sensor_type', 'machine')
    list_filter = ('sensor_type', 'machine')
    search_fields = ('sensor_name', 'machine__machine_name')


@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('machine', 'timestamp', 'sensor_value', 'unit')
    list_filter = ('machine', 'timestamp')
    search_fields = ('machine__machine_name',)
