from django.shortcuts import render
from django.http import HttpResponse
import datetime ##for testing

from . import models

import json


neighborhood_coord_dict = models.get_neighborhood_dict()

def blank(request):
	return render(request, "maps/default.html")
	##HttpResponse("Nothing here.")

def healthy_neighborhoods(request):

	##c = {"variables": models.Variable.variables,}
	##c = {"form": form,}

	form = models.Variable()
	c = {"form": form, "map": False}
	if request.method == "POST":
		form = models.Variable(request.POST)
		if form.is_valid():
			v1 = form.cleaned_data["variable_1"]
			v2 = form.cleaned_data["variable_2"]

			c["variables"] = [v1.lower(), v2.lower()]

			print("{} : {}".format(v1, v2))
			c["map"] = True
			##print(models.get_result_list(v1, v2))

			if v1 == v2 or v2 == "None":
				coef, neighborhood_list = (1, models.get_result_list(v1, v2))
			else:
				coef, neighborhood_list = models.get_result_list(v1, v2)

			c["coef"] = '{0:.3f}'.format(coef)
			print(c["coef"])

			##neighborhood_coord_dict = models.get_neighborhood_dict()

			##print(neighborhood_coord_dict.keys())
			##print(len(neighborhood_coord_dict.keys()))


			models.get_combo_dict(neighborhood_list, neighborhood_coord_dict)

			##print(neighborhood_list)
			##print(len(neighborhood_list))

			c["neighborhoods"] = neighborhood_coord_dict
			


		return render(request, "maps/healthy_neighborhoods.html", c)
	return render(request, "maps/healthy_neighborhoods_start.html", c)
	##return HttpResponse("Healthy Neighborhoods")



'''
class VariableSelectionForm(forms.ModelForm):
	class Meta:
		model = models.Variable
		fields = ["variable"]
'''