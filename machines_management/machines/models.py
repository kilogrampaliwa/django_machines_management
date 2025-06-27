from django.db import models
from django.contrib.auth.models import User

class Machine(models.Model):
    """
    Single machine description.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='machines')
    machine_name = models.CharField(max_length=100, unique=True)
    machine_location = models.CharField(max_length=100)
    machine_description = models.TextField(blank=False, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'machine_name'], name='unique_machine_per_user')
        ]
    def __str__(self):
        return f"{self.machine_name} ({self.user.username})"

class SensorData(models.Model):
    """
    Data collected from sensors attached to machines.
    """
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='sensor_data')
    timestamp = models.DateTimeField()
    sensor_value = models.FloatField()
    unit = models.CharField(max_length=20, default='Milimeters')

    class Meta:
        ordering = ['-timestamp']
        unique_together = ('machine', 'timestamp')

    def __str__(self):
        return f"{self.machine.machine_name} @ {self.timestamp}"


class Sensor(models.Model):
    sensor_name = models.CharField(max_length=100, unique=True)
    sensor_description = models.TextField(blank=False, null=False)
    sensor_type = models.CharField(
        max_length=50,
        choices=[
            ('progress', 'Progress'),
            ('min_max', 'Min/Max'),
            ('speedometer', 'Speedometer'),
            ('error_treshold', 'Error Treshold'),
            ('no_vis', 'No Visualisation'),
        ],
        default='no_vis'
    )
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='sensors')

    def __str__(self):
        return self.sensor_name