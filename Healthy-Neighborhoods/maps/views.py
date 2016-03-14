from django.shortcuts import render
from django.http import HttpResponse

from . import forms


## Initalize dictionary of neighborhood coordinates
neighborhood_coord_dict = forms.get_neighborhood_dict()
c = {"neighborhoods": neighborhood_coord_dict}


## Blank/unknown site page
def blank(request):
	return render(request, "maps/default.html")


## Main site page
def healthy_neighborhoods(request):
	c["form"] = forms.Variable()
	
	if request.method == "POST":
		if "ex_1" in request.POST:
			var_1 = "Below Poverty Level"
			var_2 = "Childhood Blood Lead Level Screening"
		elif "ex_2" in request.POST:
			var_1= "Assault (Homicide)"
			var_2 = "Per Capita Income"
		elif "ex_3" in request.POST:
			var_1 = "Dependency"
			var_2 = "Firearm-related"
		else:
			form = forms.Variable(request.POST)
			if form.is_valid():
				var_1 = form.cleaned_data["variable_1"]
				var_2 = form.cleaned_data["variable_2"]
		
		c["variables"] = [var_1.lower(), var_2.lower()]

		coef, neighborhood_list = forms.get_result_list(var_1, var_2)

		c["coef"] = '{0:.3f}'.format(coef)

		## Add color identifiers to neighborhood dictionaries
		forms.get_combo_dict(neighborhood_list, neighborhood_coord_dict)

		return render(request, "maps/healthy_neighborhoods.html", c)
	return render(request, "maps/healthy_neighborhoods_start.html", c)


## Site ocumentaion page
def documentation(request):
	return render(request, "maps/documentation.html")