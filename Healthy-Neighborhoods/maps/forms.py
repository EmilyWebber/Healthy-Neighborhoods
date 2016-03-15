from django import forms

import os
import csv
import json

from . import data_analysis
from . import mapping


def get_variables_choices():
	'''
	Read list of possible indicators from data file
	'''
	path = (os.path.dirname(os.path.abspath(__file__)))
	file_path = path +'/static/maps/Data/city_health_stats.csv'

	with open(str(file_path), "r") as f:
		reader = csv.reader(f)
		variables = sorted(f.readline().strip().split(",")[2:])

		temp = [(x,x) for x in variables]
	return temp


class Variable(forms.Form):
	variable_choices = get_variables_choices()
	
	variable_1 = forms.ChoiceField(label = "Variable 1", choices = variable_choices)
	variable_choices.append(("None", "None"))
	variable_2 = forms.ChoiceField(label = "Variable 2", choices = variable_choices)


def get_result_list(variable_1, variable_2):
	'''
	Get list of neighborhoods and their associated color identifier, given the
	selection of indicators variable_1 and variable_2
	'''

	## Case of "None" or same variable selected
	variable_2 = variable_1 if variable_2 == "None" else variable_2

	neighborhood_list = data_analysis.main(variable_1, variable_2)
	return neighborhood_list


def get_neighborhood_dict():
	'''
	Get neighborhood coordinate dictionary
	'''
	neighborhood_dict = mapping.main()
	return neighborhood_dict


def get_combo_dict(neighborhood_list, neighborhood_coord_dict):
	'''
	Add color identifier to neighborhood coordinate dictionary
	'''
	for neighborhood in neighborhood_coord_dict:
		neighborhood_coord_dict[neighborhood]["neighborhood"] = json.dumps(neighborhood)
		for name, color in neighborhood_list:
			if name == neighborhood:
				neighborhood_coord_dict[neighborhood]["clr"] = json.dumps(color)