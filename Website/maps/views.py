from django.shortcuts import render
from django.http import HttpResponse
import datetime ##for testing


def blank(request):
	return render(request, "maps/default.html")
	##HttpResponse("Nothing here.")

def healthy_neighborhoods(request):
	return render(request, "maps/healthy_neighborhoods.html")
	##return HttpResponse("Healthy Neighborhoods")

##for testing
def home_page(request):
	now = datetime.datetime.now()
	html = "<html><h1>Home page</h1><p>It is now {}.</p></html>".format(now)
	return HttpResponse(html)