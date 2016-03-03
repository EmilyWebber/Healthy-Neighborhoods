from django.shortcuts import render
from django.http import HttpResponse
import datetime ##for testing

from . import models

def blank(request):
	return render(request, "maps/default.html")
	##HttpResponse("Nothing here.")

def healthy_neighborhoods(request):

	c = {"variables": models.Variable.variables,}

	return render(request, "maps/healthy_neighborhoods.html", c)
	##return HttpResponse("Healthy Neighborhoods")

class VariableSelectionForm(forms.ModelForm):
	class Meta:
		model = models.Variable