from django.db import models

class Process(models.Model):
	Process_name = models.CharField('Process_name',max_length=10, null=True)
	Arrival_time = models.DecimalField('Arrival_time', max_digits=5, decimal_places=2, null=True)
	Burst_time = models.DecimalField('Burst_time', max_digits=5, decimal_places=2, null=True)
	Completion_time = models.DecimalField('Completion_time',max_digits=5, decimal_places=2, null=True)
	Turnaround_time = models.DecimalField('Turnaround_time', max_digits=5, decimal_places=2, null=True)
	Waiting_time = models.DecimalField('Waiting_time', max_digits=5, decimal_places=2, null=True)