# from .models import Process 
from django import forms 
  
# creating a django form 
class ProcessForm(forms.Form): 
    Process_name = forms.CharField()
    Arrival_time = forms.DecimalField()
    Burst_time = forms.DecimalField()
	 