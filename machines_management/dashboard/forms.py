from django import forms
from machines.models import Machine, Sensor

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['machine_name', 'machine_description', 'machine_location']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_machine_name(self):
        name = self.cleaned_data['machine_name']
        if self.user and Machine.objects.filter(user=self.user, machine_name=name).exists():
            raise forms.ValidationError("You already have a machine with this name.")
        return name

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['sensor_name', 'sensor_type', 'sensor_description', 'machine']
        widgets = {
            'machine': forms.HiddenInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('sensor_name')
        machine = cleaned_data.get('machine')

        if name and machine and Sensor.objects.filter(machine=machine, sensor_name=name).exists():
            self.add_error('sensor_name', 'This sensor name already exists for this machine.')

        return cleaned_data
