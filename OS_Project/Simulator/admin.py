from django.contrib import admin
from .models import Process

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('Process_name','Arrival_time','Burst_time','Completion_time','Turnaround_time','Waiting_time')
