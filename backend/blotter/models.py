from django.db import models
from datetime import datetime

# Create your models here.

class BlotterModel(models.Model):
    report_id = models.AutoField(primary_key=True)
    crime_type = models.CharField(max_length=100)
    crime_description = models.CharField(max_length=100)
    crime_datetime = models.DateTimeField()
    report_datetime = models.DateTimeField(default=datetime.utcnow())

    #objects = models.Manager()

    class Meta:
        db_table = "blotter"
        ordering = ['report_datetime']
