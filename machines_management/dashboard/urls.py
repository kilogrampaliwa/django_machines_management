from django.urls import path
from .views import dashboard, machineForm, machineDetail

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('machine-form/', machineForm, name='machine_form'),
    path('machine-detail/<int:pk>/', machineDetail, name='machine_detail'),
]