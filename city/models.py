from django.db import models
# Create your models here.

class City(models.Model):
	name = models.CharField(max_length=200, null=True)
	restrictionlevel=models.FloatField(default=1)
	'''
	1>low cases
	2>medium cases
	3>high cases
	'''
