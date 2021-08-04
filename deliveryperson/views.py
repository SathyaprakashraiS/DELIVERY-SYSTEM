from django.shortcuts import render
from store.models import Orderer
from city.models import City
from .models import *

# Create your views here.
def restrictionfinder(request):
	dmcity=request.user.city
	lor=City.object.all().filter(city=dmcity)
	obj=Orderer.object.all().filter(city=dmcity)
	return render(request,'delivery.html',{'obj':obj,'dmcity':dmcity,'lor':lor})