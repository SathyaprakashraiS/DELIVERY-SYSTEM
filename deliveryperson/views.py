from django.shortcuts import render
from store.models import *
from city.models import *
from .models import *
from django.db.models.functions import Lower

# Create your views here.
def restrictionfinder(request):
	dboycity=request.user.city
	dlist=Orderer.objects.all().filter(city=dboycity.lower())
	lor=City.objects.all().filter(name=dboycity.lower())
	'''
	dboycity=request.user.city
	dlist=Orderer.objects.all().filter(city=Lower(dboycity))
	lor=City.objects.all()
	'''
	return render(request,'delivery.html',{'dboycity':dboycity,'dlist':dlist,'lor':lor})