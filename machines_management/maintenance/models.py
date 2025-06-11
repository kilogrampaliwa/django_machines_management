from django.db import models
from machines.models import Machine

class MaintenanceLog(models.Model):
    """
    Intervention log for machine maintenance.
    """
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='maintenance_logs')
    performed_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    
    def __str__(self):
        return f"Maintenance on {self.machine.name} at {self.performed_at}"
