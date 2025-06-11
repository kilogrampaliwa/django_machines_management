from django.db import models
from machines.models import Machine


class FailurePrediction(models.Model):
    """
    Saves data and makes predictions about machine failures.
    This model stores the predicted failure risk and time to failure for each machine.
    """
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='predictions')
    predicted_at = models.DateTimeField(auto_now_add=True)
    failure_risk = models.FloatField()
    predicted_time_to_failure = models.DurationField(null=True, blank=True)
    
    def __str__(self):
        return f"Prediction for {self.machine.name} at {self.predicted_at}"
