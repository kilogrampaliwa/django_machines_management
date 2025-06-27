from django.urls import path
from .views import dashboard, machineForm

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('machine-form/', machineForm, name='machine_form'),
]