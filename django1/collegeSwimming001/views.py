from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Meet
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
	
def meet(request, meet_id):
	m = Meet.objects.get(pk=meet_id)
	return HttpResponse(m)