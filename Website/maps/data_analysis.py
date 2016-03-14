import csv
import os
import numpy as np
from . import color_support
import plotly.plotly as py
import plotly.graph_objs as go

path = (os.path.dirname(os.path.abspath(__file__)))
FILE = path +'/static/maps/Data/city_health_stats.csv'

py.sign_in('healthy_neighborhoods','d806djbyh8')

DEFAULT = None

# necessary specifications to fit plotly matrix
ROWS = 9
COLS = 3
X_ID = 0
Y_ID = 1
NAME_ID = 2


def get_lists(var1, var2):
	'''
	Takes two variable strings
	Returns three lists:
        xs: list of floats 
        ys: list of floats
        rt: list of tuples (name, x, y)
    Xs and ys will not have any DEFAULT, but rt has DEFAULT for every missing values in the csv 
        Which is used to generate gray color in google maps
        But each of them needs to be skipped for the scatter array
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

def initialize_scatter(rt):
    '''
    Takes an empty list, 
    Initializes a 9-3 array
    '''
    for i in range(ROWS):
        l = []
        for j in range(COLS):
            l.append([])
        rt.append(l)
    return rt

def get_scatter_array(var1, var2):
 	'''
    Takes two variables from plot_graph
 		Returns an array and a list of colors
            scatter: a 9-3 array built to match plotly specifications
            list of colors: list of strings, where the index space of each color matches
                the index space of the correct color quadrant, 0-8
 	'''
    # if the second variable is default, overwrite it as the first
 	if var2 == DEFAULT:
 		var2 = var1

 	xs, ys, rt = get_lists(var1, var2)
 	scatter = initialize_scatter([])
 	for (name, x, y) in rt:

        # only add a value to the scatter array if the measurement is not DEFAULT,
        # which means the observation is actually present for that variable

 		if (x != DEFAULT) and (y != DEFAULT):
 			inner = scatter[get_color(x, y, xs, ys, True)]
 			inner[X_ID].append(x)
 			inner[Y_ID].append(y)
 			inner[NAME_ID].append(name)
 	return scatter, color_support.scatter_color_list

def get_color(x, y, xs, ys, scatter = False):
    '''
    Takes one x observation, one y observation, a list of x measurements and a list of y measurements,
        and a boolean value for whether or not the color should match the scatter plot array
        Walks through the short list of thresholds for the x observation and the y observation
    Returns a single string that corresponds to the correct color for that neighborhood
    '''
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

		if (x == DEFAULT) or (y == DEFAULT):
			final.append((name, color_support.color_matrix[DEFAULT]))
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
	x = get_val(row[headers[var1]])
	y = get_val(row[headers[var2]])
	rt.append((name, x, y))
	if (y != DEFAULT) and (x != DEFAULT):
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
		return DEFAULT

def main(variable_1, variable_2 = DEFAULT):
    '''
    How this file interacts with Django framework
    Takes two variables that are passed from user input
    Calls plot_graph
    And returns google maps data structure
    '''
    plot_graph(variable_1, variable_2)
    return google_maps(variable_1, variable_2)

def compare(var1, var2):
	'''
	Takes two variable names and returns the correlation coefficient
    Useful for systematically comparing lists of variables
    We used this in generating some of our analysis,
        such as finding the strongest health correlation for each economic indicator
    But it's not explicitly tied to the website visualizations
	'''
	xs, ys, rt = get_lists(var1, var2)
	return get_correlation_coefficient(xs, ys)

def create_trace(i, val, colors):
    '''
    Takes index, list of X, Y, and neighborhood values and creates a trace object with color
    '''
    trace = "var" + str(i)
    color = colors[i]
    x_vals = val[X_ID]
    if len(x_vals) == 0:
        return None
    y_vals = val[Y_ID]
    neighborhoods = val[NAME_ID]
    trace = go.Scatter(
    x = x_vals,
    y = y_vals,
    mode = 'markers',
    marker = dict(color = color, size = 12,
                line = dict(width = 1)
               ), 
      text = neighborhoods,
      name = "")
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
    showlegend = False,
    title = graph_title,
    hovermode = 'closest',
    xaxis = dict(
        title = var1,
        ticklen = 5,
        zeroline = False,
        gridwidth = 2,
    ),
    yaxis = dict(
        title = var2,
        ticklen = 5,
        gridwidth = 2,
    ),
  )
    fig = go.Figure(data = data, layout = layout)
    py.iplot(fig, filename = 'healthy-neighborhoods')