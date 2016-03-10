import sys
import csv
import correlations

SOCIO_FILE = 'Data/Socioeconomic-Indicators.txt'
HEALTH_FILE = 'Data/Health-Indicators.txt'

socio = []
health = []
top_socio = {}

for i in open(SOCIO_FILE, 'r').readlines():
	socio.append(i.strip('\n'))

for i in open(HEALTH_FILE, 'r').readlines():
	health.append(i.strip('\n'))

# get the top 3 health indicators with strongest correlations
def ranking_algo():
	for s in socio:

		top_health_correlations = [(0,0), (0,0), (0,0)]
		
		for h in health:

			beta = correlations.compare(s, h)
		
			for i, tup in enumerate(top_health_correlations):
				print (tup[0])

				if abs(beta) > tup[1]:
					top_health_correlations[i] = (h, beta)

		top_socio[s] = top_health_correlations

	print (top_socio)



# for each in health:
	# get the top 3 socio indicators

if __name__ == "__main__":
	ranking_algo()