from django.db import models

# Create your models here.
class Persondetails(models.Model):
	name=models.CharField(max_length=200)
	phonenumber=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	city=models.CharField(max_length=200)