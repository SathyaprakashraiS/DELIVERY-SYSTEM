from django.shortcuts import render
from store.models import *
from city.models import *
from .models import *
from django.db.models.functions import Lower
from itertools import chain
from django.db.models import F

# Create your views here.
def restrictionfinder(request):
	dboycity=request.user.city
	linkgen1=Orderer.objects.values_list('add1link')
	linkgen2=Orderer.objects.values_list('add2link')
	dlist=Orderer.objects.all().filter(city=dboycity.lower())
	testlist=Orderer.objects.all().filter(city=dboycity.lower())
	clist=Area.objects.all().filter(city__name=dboycity.lower())
	alist=Orderer.objects.all().filter(city=dboycity.lower())
	pervaikala=[]
	for string in clist:
		obj=[]
		alist=alist.filter(address2__contains=string)
		obj=Area.objects.all()
		obj=obj.filter(areaname__contains=string)
		if testlist.filter(address2__contains=string):
			testlist.filter(address2__contains=string).update(reslev=string.restrictionlevel)
	lor=City.objects.all().filter(name=dboycity.lower())
	result=list(chain(dlist,pervaikala))

	'''
	
	result=list(chain(obj,pal,veg,vag,ket,med))


	dboycity=request.user.city
	dlist=Orderer.objects.all().filter(city=Lower(dboycity))
	lor=City.objects.all()
	'''
	return render(request,'delivery.html',{'dboycity':dboycity,'dlist':dlist,'lor':lor,'linkgen1':linkgen1,'linkgen2':linkgen2,'alist':alist,'obj':obj,'result':result,'testlist':testlist})

def unidel(request):
	idname=request.GET['orderername']
	obj=Orderer.objects.all().filter(name=idname)
	return render(request,'unidel.html',{'idname':idname})	