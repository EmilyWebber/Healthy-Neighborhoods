from django.shortcuts import render
from django.http import HttpResponse
import datetime ##for testing

from . import models

def blank(request):
	return render(request, "maps/default.html")
	##HttpResponse("Nothing here.")

def healthy_neighborhoods(request):

	##c = {"variables": models.Variable.variables,}
	##c = {"form": form,}

	form = models.Variable()
	if request.method == "POST":
		form = models.Variable(request.POST)
		if form.is_valid():
			print(form.cleaned_data["variable_1"])
			print(form.cleaned_data["variable_2"])

	return render(request, "maps/healthy_neighborhoods.html", {"form": form,})
	##return HttpResponse("Healthy Neighborhoods")



def map(request):
	return render(request, "maps/map")
'''
class VariableSelectionForm(forms.ModelForm):
	class Meta:
		model = models.Variable
		fields = ["variable"]
'''