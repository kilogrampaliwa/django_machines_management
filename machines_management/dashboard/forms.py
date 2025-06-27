from django import forms
from machines.models import Machine, Sensor

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['machine_name', 'machine_description', 'machine_location']


class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['sensor_name', 'sensor_type', 'sensor_description', 'machine']