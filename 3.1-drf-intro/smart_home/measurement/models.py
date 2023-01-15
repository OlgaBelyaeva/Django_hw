from django.db import models

class Sensor(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    date_measurement = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='measurement/images', null=True, blank=True)

