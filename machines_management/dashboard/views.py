from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MachineForm
from django.http import JsonResponse
# Create your views here.

@login_required
def dashboard(request):
    machines = request.user.machines.all()
    parts = []
    return render(request, 'dashboard/dashboard.html', {
        'machines': machines,
        'parts': parts,
    })

@login_required
def machineForm(request):
    if request.method == "POST":
        form = MachineForm(request.POST)
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