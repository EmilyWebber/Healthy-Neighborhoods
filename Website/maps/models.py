from __future__ import unicode_literals
##from django.db import models
from django import forms
import os
import csv

import sys

from django.core.management import call_command

from Analysis import correlations
from Mapping import polygon_color

##sys.path.insert(0, "/Healthy-Neighborhoods/Analysis/")
##print(sys.path)
##from Analysis import correlations


base_path = os.path.dirname(__file__)
#file_path = os.path.abspath(os.path.join(base_path, "..", "..", "Analysis/")))


def get_variables_choices():
	file_path = str(os.path.abspath(os.path.join(base_path, "Analysis/Data/city_health_stats.csv" )))

	with open(file_path, "rU") as f:
		reader = csv.reader(f)
		variables = f.next().strip().split(",")[2:]

		temp = [(x,x) for x in variables]
	return temp
	'''
	with open(file_path, 'rU') as f:
		fields = csv.reader(f)
		cols =  next(fields)
	print(cols)
	return cols[2:]
	'''
	
class Variable(forms.Form):
	variable_choices = get_variables_choices()
	variable_1 = forms.ChoiceField(label = "Variable 1", choices = variable_choices)
	variable_choices.append(("None", "None"))
	variable_2 = forms.ChoiceField(label = "Variable 2", choices = variable_choices)
	##= forms.CharField(max_length = 64)


def get_result_list(variable_1, variable_2):
	##file_path = os.path.abspath(os.path.join(base_path, "..", "..", "Analysis"))
	##file_name = os.path.join(file_path, "correlations.py")
	##execfile(file_name)
	##print(file_path)
	##from file_path import correlations

	##os.chdir(os.path.abspath(os.path.join(base_path, "..", "..", "Analysis" )))

	##import correlations

	variable_2 = None if variable_1 == variable_2 else variable_2
	variable_2 = None if variable_2 == "None" else variable_2
	##print(correlations.main(variable_1, variable_2))

	print(variable_1)
	print(variable_2)
	neighborhood_list = correlations.main(variable_1, variable_2)
	return neighborhood_list
	##file_path = os.path.abspath(os.path.join(base_path, "..", "..", "Analysis/correlations.py" ))
	##os.system(file_path)

def get_neighborhood_dict():
	neighborhood_dict = polygon_color.main()
	return neighborhood_dict

'''
class Neighborhood(models.Model):
	pass
	##name = models.CharField(max_length = 200)
'''