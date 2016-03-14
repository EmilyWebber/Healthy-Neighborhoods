import csv
import sys
import numpy as np
import numpy as np
import os
from . import color_support
import plotly.plotly as py
import plotly.graph_objs as go

path = (os.path.dirname(os.path.abspath(__file__)))
FILE = path +'/static/maps/Data/city_health_stats.csv'
py.sign_in('healthy_neighborhoods','d806djbyh8')
VALUES = ["var0", "var1", "var2","var3", "var4", "var5", "var6", "var7", "var8"]
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
 	return scatter, color_support.scatter_color_list

def get_color(x, y, xs, ys, scatter = False):

    for idx, (low, high) in enumerate(get_thresholds(xs)):
    	if (x >= low) and (x <= high):
    		x_id = color_support.index_matrix[idx]
    for idx, (low, high) in enumerate(get_thresholds(ys)):
    	if (y >= low) and (y <= high):
    		y_id = color_support.index_matrix[idx]
    if not scatter:
    	return color_support.color_matrix[(x_id, y_id)]
    return color_support.scatter_matrix[(x_id, y_id)]

def assign_colors(xs, ys, rt, final):
	'''
	Takes a list of tuples, assigns the correct color
	'''
	for (name, x, y) in rt:

		if (x == None) or (y == None):
			final.append((name, color_support.color_matrix[None]))
		else:
			final.append((name, get_color(x, y, xs, ys, False)))
	coeff = get_correlation_coefficient(xs, ys)
	return (coeff, final)

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
	x = get_val(row[headers[var1]])
	y = get_val(row[headers[var2]])
	rt.append((name, x, y))
	if (y != None) and (x != None):
		ys.append(y)
		xs.append(x)

def get_val(x):
	'''
	Takes a measurement from the row, tries to convert to float and add to values_list
	If not, returns None
	'''
	try:
		return float(x)
	except:
		return None

def main(variable_1, variable_2 = None):

	plot_graph(variable_1, variable_2)

	plot_graph(variable_1, variable_2)
	#scatterplot.plot_graph(variable_1, variable_2)
	plot_graph(variable_1, variable_2)


	plot_graph(variable_1, variable_2)

	return google_maps(variable_1, variable_2)

def compare(var1, var2):
	'''
	Takes two variable names and returns the correlation coefficient
	'''
	xs, ys, rt = get_lists(var1, var2)
	return get_correlation_coefficient(xs, ys)


def create_trace(i, val, colors):
    '''
    Takes index, list of X, Y, and neighborhood values and creates a trace object
    with color
    '''
    trace = VALUES[i]
    color = colors[i]
    x_vals = val[0]
    if len(x_vals) == 0:
        return None
    y_vals = val[1]
    neighborhoods = val[2]
    trace = go.Scatter(
    x= x_vals,
    y= y_vals,
    mode='markers',
    marker=dict(color=color, size=12,
                line=dict(width=1)
               ), 
      text=neighborhoods,
      name="")
    return trace

def plot_graph(var1, var2):
    '''
    input: Receives two string variables from django
         Receives scatter, list of 9 lists, each interior list with an x, y, and neighborhood get_scatter_array 
         Receives colors, an ordered list corresponding with the interior lists of scatter
    output: Creates a trace for each of 9 lists , append to data file and creating scatterplot 
    '''

    scatter, colors = get_scatter_array(var1, var2)
    graph_title = var1 + ' vs ' + var2
    data = []
    for i, val in enumerate(scatter):
        trace = create_trace(i, val, colors)
        if trace:
          data.append(trace)
    layout = go.Layout(
    showlegend=False,
    title= graph_title,
    hovermode='closest',
    xaxis=dict(
        title=var1,
        ticklen=5,
        zeroline=False,
        gridwidth=2,
    ),
    yaxis=dict(
        title=var2,
        ticklen=5,
        gridwidth=2,
    ),
  )
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='healthy-neighborhoods')
