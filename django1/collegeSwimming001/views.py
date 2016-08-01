from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.db.models import Count

from grapher import calculateScores
from .models import Meet, Swimmer, Time
from .forms import TeamScheduleForm
from builder import buildSchedule


def index(request):  
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = TeamScheduleForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			buildSchedule(form.cleaned_data['team_name'])
			return HttpResponseRedirect('/meet/%d' %Meet.objects.latest('id').id )

    # if a GET (or any other method) we'll create a blank form
	else:
		form = TeamScheduleForm()

	return render(request, 'collegeSwimming001/scheduleForm.html', {'form': form})
	
def meetDetails(request, meet_id):
	m = Meet.objects.filter(pk=meet_id).first()
	events= Time.objects.filter(meet__id= meet_id).values('event__distance', 'event__stroke', 'event__id').distinct()
	template = loader.get_template('collegeSwimming001/meetDetailsPage.html')
	context = {
		'meet' : m,
		'events':events
	}
	return HttpResponse(template.render(context,request))

def meetWithEvent(request, meet_id, event_id):
	event = Time.objects.filter(meet__id=meet_id, event__id=event_id).order_by('place')
	template = loader.get_template('collegeSwimming001/eventDetailsPage.html')
	context = {
		'event' : event
	}
	return HttpResponse(template.render(context,request))
	
	
def meets(request):
	m = Meet.objects.all().order_by('-start_date')
	template = loader.get_template('collegeSwimming001/meetPage1.html')
	context = {
		'meets' : m
	}
	return HttpResponse(template.render(context,request))
	
def swimmers(request):
	swimmers = Swimmer.objects.all().values('name','id').annotate(total=Count('time')).filter(total__gte=3	).order_by('total')
	template = loader.get_template('collegeSwimming001/swimmersPage.html')
	context ={
		'swimmers':swimmers
	}
	return HttpResponse(template.render(context,request))

def swimmer(request, swimmer_id):
	sw = Time.objects.filter(swimmer=swimmer_id)

	scores = calculateScores(swimmer_id)
	
	swimmerName = Swimmer.objects.filter(pk=swimmer_id).first().name
	template = loader.get_template('collegeSwimming001/swimmerRadarChart.html')
	context = {
		'swimmer_name' : swimmerName,
		'swimmer_id' : swimmer_id,
		'scores' : scores
	}
	return HttpResponse(template.render(context),request)

def swimmerChart(request, swimmer_id):
	scores = calculateScores(swimmer_id)
	
	return JsonResponse(scores)