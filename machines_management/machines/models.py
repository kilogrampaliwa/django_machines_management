from django.db import models

class Machine(models.Model):
    """
    Single machine description.
    """
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class SensorData(models.Model):
    """
    Data collected from sensors attached to machines.
    """
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='sensor_data')
    timestamp = models.DateTimeField()
    sensor_value = models.FloatField()
    unit = models.CharField(max_length=20, default='Celsius')
    class Meta:
        ordering = ['-timestamp']
        unique_together = ('machine', 'timestamp')

    def __str__(self):
        return f"{self.machine.name} @ {self.timestamp}"
