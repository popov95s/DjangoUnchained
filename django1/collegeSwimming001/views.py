from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("This is the index page")

	
def event(request, event_id):
    response = "This is the details page for event %s."
    return HttpResponse(response % event_id)