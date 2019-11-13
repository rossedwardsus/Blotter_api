from django.db import models

# Create your models here.

class Blotter(models.Model):
    reporting_id = models.IntegerField(primary_key=True)
    accident_type = models.DateTimeField(auto_now_add=True)
    observation_type = models.CharField(max_length=100)
    kill_type = models.CharField(max_length=100)
    group_type = models.CharField(max_length=100)
    number_of_tuskers = models.CharField(max_length=100, blank=True, default='')
    number_of_tots = models.TextField()
    cause_of_death = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    #sex = models.CharField(max_length=100)
    
    reporting_datetime = models.DateTimeField()

    #objects = models.Manager()

    class Meta:
        db_table = "blotter"
        ordering = ['reporting_datetime']
