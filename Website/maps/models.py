from __future__ import unicode_literals

from django.db import models

# Create your models here.

VARIABLES = (("CHO", "childhood obesity"), ("DBS", "diabetes"), ("HPT", "hypertension"), ("GRS", "grocery stores"),)


class Variable(models.Model):
	#value = models.FloatField()
	name = models.CharField(max_length = 50, choices = VARIABLES)

class Neighborhood(models.Model):
	name = models.CharField(max_length = 200)

	def __str__(self):
		return name