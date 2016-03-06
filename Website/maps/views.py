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
			neighborhood_list = models.get_result_list(v1, v2)


			neighborhood_dict = models.get_neighborhood_dict()

			##c["neighborhoods"] = {'Uptown': [json.dumps({'lat': 41.891485, 'lng': -87.614774}), json.dumps({'lat': 41.891376, 'lng': -87.647737}), json.dumps({'lat': 41.879554, 'lng': -87.645529}), json.dumps({'lat': 41.879982, 'lng': -87.617570})], 'Hyde Park': [json.dumps({'lat': 41.802735, 'lng': -87.580518}), json.dumps({'lat': 41.802261, 'lng': -87.616279}), json.dumps({'lat': 41.785613, 'lng': -87.615723}), json.dumps({'lat': 41.786501, 'lng': -87.577180})]}
			c["neighborhoods"] = {'Uptown': [[41.891485, -87.614774], [41.891376, -87.647737], [41.879554, -87.645529], [41.879982, -87.617570]], 'Hyde Park': [[41.802735, -87.580518], [41.802261, -87.616279], [41.785613, -87.615723], [41.786501, -87.577180]]}
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