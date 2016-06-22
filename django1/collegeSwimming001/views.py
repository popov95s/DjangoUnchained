from django.shortcuts import render
from django.http import HttpResponse

from .models import Meet

def index(request):
	return HttpResponse("This is the index page")

	
def meet(request, meet_id):
	m = Meet.objects.get(pk=meet_id)
	return HttpResponse(m.name)