from __future__ import unicode_literals
from django.db import models
import os

class Variable(models.Model):
	base_path = os.path.dirname(__file__)
	file_path = os.path.abspath(os.path.join(base_path, "..", "..", "Analysis/Data/city_health_stats.csv" ))

	with open(file_path) as f:
		variables = f.readline().strip().split(",")[2:]


class Neighborhood(models.Model):
	name = models.CharField(max_length = 200)

def __str__(self):
	return name