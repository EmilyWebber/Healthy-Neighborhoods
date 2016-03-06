import csv
import sys
import City
import support
import csv

FILE = 'Data/city_health_stats.csv'
DEFAULT_KEY = None
DEFAULT_VALUE = []

def go(var1, var2, rt, xs, ys, headers):
	with open (FILE,'rU') as f:
		fields = csv.reader(f)
		for i, e in enumerate(next(fields)):
			headers[e] = i
		for row in fields:
			add_to_lists(row, xs, ys, rt, headers, var1, var2)
	return assign_colors(xs, ys, rt, [])

def assign_colors(xs, ys, rt, final):
	'''
	Takes a list of tuples, assigns the correct color
	'''
	# no y variables
	if len(ys) == 0:
		for name, x in rt:
			for idx, (low, high) in enumerate(get_thresholds(xs)):
				if (x >= low) and (x <= high):
					x_id = support.index_matrix[idx]
			rt.append((name, support.color_matrix[(m_idx, DEFAULT_KEY)]))
		return rt

	for (name, x, y) in rt:
		for idx, (low, high) in enumerate(get_thresholds(xs)):
		 	if (x >= low) and (x <= high):
		 		x_id = support.index_matrix[idx]
		for idx, (low, high) in enumerate(get_thresholds(ys)):
		 	if (y >= low) and (y <= high):
		 		y_id = support.index_matrix[idx]
		final.append((name, support.color_matrix[(x_id, y_id)]))

	return final


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
		if y != None:
			ys.append(y)
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
		values_list.append(float(x))
		return float(x)
	except:
		return None


def main(variable_1, variable_2 = None):
	return go(variable_1, variable_2, [], [], [], {})


if __name__ == "__main__":
	if len(sys.argv) != 3:
	    sys.exit(1)

	print(go(sys.argv[1],sys.argv[2], [], [], [], {}))
