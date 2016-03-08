from django.shortcuts import render
from django.http import HttpResponse
import datetime ##for testing

from . import models

import json

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
			coef, neighborhood_list = models.get_result_list(v1, v2)

			neighborhood_coord_dict = models.get_neighborhood_dict()

			print(neighborhood_coord_dict.keys())
			print(len(neighborhood_coord_dict.keys()))


			models.get_combo_dict(neighborhood_list, neighborhood_coord_dict)

			print(neighborhood_list)
			print(len(neighborhood_list))
			'''
			for neighborhood in neighborhood_coord_dict:
				neighborhood_coord_dict[neighborhood]["clr"] = json.dumps('#C8011E')
				neighborhood_coord_dict[neighborhood]["name"] = neighborhood
			'''
			c["neighborhoods"] = neighborhood_coord_dict
			
			##print(type(c["neighborhoods"]))
	##print(c["neighborhoods"])
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