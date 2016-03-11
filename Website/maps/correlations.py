import csv
import sys

import numpy as np

#FILE = 'Data/city_health_stats.csv'

import numpy as np
import os

##base_path = os.path.dirname(__file__)
##FILE = os.path.abspath(os.path.join(base_path, "Data/city_health_stats.csv" ))
FILE = 'static/maps/city_health_stats.csv'

from . import support
from . import scatterplot




DEFAULT_KEY = None
DEFAULT_VALUE = []

def get_lists(var1, var2):
	'''
	Takes two variable strings
	Returns a list of xs, ys, and a list of tuples (name, x)
	'''
	xs = []
	ys = []
	rt = []
	headers = {}
	with open (FILE,'rU') as f:
		fields = csv.reader(f)
		for i, e in enumerate(next(fields)):
			headers[e] = i
		for row in fields:
			add_to_lists(row, xs, ys, rt, headers, var1, var2)
	return xs, ys, rt

def google_maps(var1, var2):
	'''
	Takes two variables, 
	Returns a tuple
		(correlation coefficient, list of tuples)
	'''
	xs, ys, rt = get_lists(var1, var2)
	return assign_colors(xs, ys, rt, [])

def get_correlation_coefficient(xs, ys):
	'''
	Takes both xs and ys, finds the correlation coefficient and adds to final list
	'''
	return np.corrcoef(xs, ys)[1,0]

def initialize_scatter():
	rt = []
	for i in range(9):
		l = []
		for j in range(3):
			l.append([])
		rt.append(l)
	return rt

def get_scatter_array(var1, var2):
 	'''
 	Is called by scatterplot.py
 		Returns an array and a list
 	'''
 	if var2 == None:
 		var2 = var1

 	xs, ys, rt = get_lists(var1, var2)
 	scatter = initialize_scatter()

 	# only add neighborhood to array if both x and y are not None
 	for (name, x, y) in rt:
 		if (x != None) and (y != None):
 			# print ("assigning to ninth quadrant {}".format(get_color(x, y, xs, ys, True)))
 			inner = scatter[get_color(x, y, xs, ys, True)]
 			inner[0].append(x)
 			inner[1].append(y)
 			inner[2].append(name)
 	return scatter, support.scatter_color_list

def get_color(x, y, xs, ys, scatter = False):

    for idx, (low, high) in enumerate(get_thresholds(xs)):
    	if (x >= low) and (x <= high):
    		x_id = support.index_matrix[idx]
    for idx, (low, high) in enumerate(get_thresholds(ys)):
    	if (y >= low) and (y <= high):
    		y_id = support.index_matrix[idx]
    if not scatter:
    	return support.color_matrix[(x_id, y_id)]
    return support.scatter_matrix[(x_id, y_id)]

def assign_colors(xs, ys, rt, final):
	'''
	Takes a list of tuples, assigns the correct color
	'''
	# no y variables

	if xs == ys:
		for name, x in rt:

			if x == None:
				final.append((name, support.color_matrix[None]))
			else:

				for idx, (low, high) in enumerate(get_thresholds(xs)):
					if (x >= low) and (x <= high):
						x_id = support.index_matrix[idx]
		
				final.append((name, support.color_matrix[(x_id, DEFAULT_KEY)]))
		
		return final

	for (name, x, y) in rt:

		if (x == None) or (y == None):
			final.append((name, support.color_matrix[None]))
		else:
			final.append((name, get_color(x, y, xs, ys, False)))

	return (get_correlation_coefficient(xs, ys), final)

def get_thresholds(xs):
	'''
	Takes a list of numerical values, returns a list of 3 tuples assigning thresholds 
	'''
	low = min(xs)
	high = max(xs)
	m1 = (high-low)/3 + low
	m2 = 2 * (high - low)/3 + low
	return [(low, m1), (m1, m2), (m2, high)]

def add_to_lists(row, xs, ys, rt, headers, var1, var2):
	'''
	Takes a row, a list of xs, ys, rt, dictionary of headers, two variables
	Adds to lists appropriately
	'''
	name = row[1]
	x = get_val(row[headers[var1]], xs)

	if var2 != None:
		y = get_val(row[headers[var2]], ys)
		rt.append((name, x, y))
		if (y != None) and (x != None):
			ys.append(y)
			xs.append(x)
	else:
		rt.append((name, x))
		if x != None:
			xs.append(x)

def get_val(x, values_list):
	'''
	Takes a measurement from the row, tries to convert to float and add to values_list
	If not, returns None
	'''
	try:
		return float(x)
	except:
		return None

def main(variable_1, variable_2 = None):
	#scatterplot.plot_graph(variable_1, variable_2)
	return google_maps(variable_1, variable_2)

def compare(var1, var2):
	'''
	Takes two variable names and returns the correlation coefficient
	'''

	xs, ys, rt = get_lists(var1, var2)
	return get_correlation_coefficient(xs, ys)

if __name__ == "__main__":
	if len(sys.argv) != 3:
	    sys.exit(1)

	# print(google_maps(sys.argv[1],sys.argv[2]))

	# print (get_scatter_array(sys.argv[1],sys.argv[2]))

	# compare(sys.argv[1],sys.argv[2])
