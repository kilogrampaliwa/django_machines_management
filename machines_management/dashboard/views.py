from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from machines.models import Machine, Sensor
from .forms import MachineForm, SensorForm
from django.http import JsonResponse
# Create your views here.

@login_required
def dashboard(request):
    machines_qs = request.user.machines.all()
    machines = [
        {
            "id": machine.id,
            "name": machine.machine_name,
            "description": machine.machine_description,
            "details": [
                f"Location: {machine.machine_location}",
            ],
        }
        for machine in machines_qs
    ]
    return render(request, 'dashboard/dashboard.html', {
        'machines': machines,
    })


@login_required
def machineForm(request):
    if request.method == "POST":
        form = MachineForm(request.POST, user=request.user)
        if form.is_valid():
            machine = form.save(commit=False)
            machine.user = request.user
            machine.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = MachineForm()
        return render(request, 'forms/machine_form.html', {'form': form})

def machineDetail(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    sensors = Sensor.objects.filter(machine=machine)
    return render(request, 'dashboard/partials/machine_detail.html', {
        'machine': machine,
        'sensors': sensors
    })

@login_required
def sensorForm(request, machine_id):
    machine = get_object_or_404(Machine, pk=machine_id, user=request.user)

    if request.method == "POST":
        form = SensorForm(request.POST)
        if form.is_valid():
            sensor = form.save(commit=False)
            sensor.machine = machine
            sensor.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = SensorForm(initial={'machine': machine})
        return render(request, 'forms/sensor_form.html', {'form': form, 'machine': machine})
