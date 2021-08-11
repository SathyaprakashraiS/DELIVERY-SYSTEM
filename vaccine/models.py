from django.db import models
from ecommerce import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class Vform(models.Model):
	name = models.CharField(max_length=200, null=True)
	vacday=models.DateField("mm/dd/yyyy",auto_now_add=False,auto_now=False,blank=False,null=True)
	dosecount=models.IntegerField(default=0)
	prooffile=models.FileField(upload_to='images', default='images/none.pdf')

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

	def __str__(self):
		return (self.name)
