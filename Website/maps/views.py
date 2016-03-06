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
	c = {"form": form}
	if request.method == "POST":
		form = models.Variable(request.POST)
		if form.is_valid():
			v1 = form.cleaned_data["variable_1"]
			v2 = form.cleaned_data["variable_2"]
			neighborhood_list = models.get_result_list(v1, v2)
			print(neighborhood_list)

			neighborhood_dict = models.get_neighborhood_dict()
			print(neighborhood_dict.keys())

			c["neighborhoods"] = neighborhood_dict
			##print(c["neighborhoods"]["Uptown"])
	return render(request, "maps/healthy_neighborhoods.html", c)
	##return HttpResponse("Healthy Neighborhoods")



def map(request):
	return render(request, "maps/map")
'''
class VariableSelectionForm(forms.ModelForm):
	class Meta:
		model = models.Variable
		fields = ["variable"]
'''