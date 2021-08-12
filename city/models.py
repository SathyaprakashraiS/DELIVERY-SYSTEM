from django.db import models
# Create your models here.

class City(models.Model):
	name = models.CharField(max_length=200, null=True)
	def __str__(self):
		return "%s" % (self.name)
	'''
	1>low cases
	2>medium cases
	3>high cases
	'''

class Area(models.Model):
	city = models.ForeignKey(City,on_delete=models.CASCADE)
	areaname = models.CharField(max_length=200, null=True)
	restrictionlevel=models.FloatField(default=1)
	    
	def __str__(self):
    	 return self.areaname
	class Meta:
		 ordering = ['areaname']

'''
class City(models.Model):
	name = models.CharField(max_length=200, null=True)
	restrictionlevel=models.FloatField(default=1)
	''
	''
	1>low cases
	2>medium cases
	3>high cases
	'''
