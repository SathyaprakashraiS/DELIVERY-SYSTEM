from django.shortcuts import render

# Create your views here.
def vacform(request):
	return render(request,"vacform.html",{})