from django.db import models

# Create your models here.
class EquipmentDataset(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    total_count = models.IntegerField()
    avg_flowrate = models.FloatField()
    avg_pressure = models.FloatField()
    avg_temperature = models.FloatField()