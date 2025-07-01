from django.urls import path
from .views import dashboard, machineForm, machineDetail, sensorForm

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('machine-form/', machineForm, name='machine_form'),
    path('machine-detail/<int:pk>/', machineDetail, name='machine_detail'),
    path('sensor-form/<int:machine_id>/', sensorForm, name='sensor_form')

]