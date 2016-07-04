import requests
import re 
from collections import defaultdict
from bs4 import BeautifulSoup
import json
from six.moves import urllib
from .models import Meet, Team, Conference, Division

list = {'SMU':'http://www.smumustangs.com/sports/m-swim/sched/smu-m-swim-sched.html','TCU':'http://www.gofrogs.com/sports/c-swim/sched/tcu-c-swim-sched.html','ECU':'http://www.ecupirates.com/sports/c-swim/sched/ecu-c-swim-sched.html'
		,'Cinn':'http://www.gobearcats.com/sports/c-swim/sched/cinn-c-swim-sched.html', 'UConn' :'http://www.uconnhuskies.com/sports/m-swim/sched/conn-m-swim-sched.html','Villanova':'http://www.villanova.com/sports/c-swim/sched/nova-c-swim-sched.html', 'UT' : 'http://www.texassports.com/schedule.aspx?path=mswim',
		'Cal' : 'http://www.calbears.com/SportSelect.dbml?DB_OEM_ID=30100&SPID=126526&SPSID=749488&DB_OEM_ID=30100', 'Florida' : 'http://floridagators.com/schedule.aspx?path=swimmingdiving-men', 'NC State' : 'http://gopack.com/schedule.aspx?path=swim',
		'UGA' : 'http://www.georgiadogs.com/sports/c-swim/sched/geo-c-swim-sched.html', 'Michigan' : 'http://www.mgoblue.com/sports/m-swim/sched/mich-m-swim-sched.html', 'Stanford' : 'http://www.gostanford.com/SportSelect.dbml?&DB_OEM_ID=30600&SPID=130813&SPSID=789224',
		'Auburn' : 'http://www.auburntigers.com/sports/c-swim/sched/aub-c-swim-sched.html', 'Indiana' : 'http://iuhoosiers.com/schedule.aspx?path=mswim', 'Louisville' : 'http://www.gocards.com/schedule.aspx?path=swim',
		'Arizona' : 'http://www.arizonawildcats.com/SportSelect.dbml?&DB_OEM_ID=30700&SPID=127126&SPSID=790511', 'USC' : 'http://www.usctrojans.com/sports/m-swim/sched/usc-m-swim-sched.html', 'Ohio State' : 'http://www.ohiostatebuckeyes.com/sports/w-swim/sched/osu-w-swim-sched.html',
		'Alabama' : 'http://www.rolltide.com/sports/c-swim/sched/alab-c-swim-sched.html', 'Missouri' : 'http://mutigers.com/schedule.aspx?path=mswim','Wisconsin' : 'http://www.uwbadgers.com/schedule.aspx?path=swim', 'Harvard' : 'http://gocrimson.com/sports/mswimdive/2015-16/schedule',
		'Princeton' : 'http://www.goprincetontigers.com/SportSelect.dbml?&DB_OEM_ID=10600&SPID=4221&SPSID=46493', 'Penn' : 'http://www.pennathletics.com/SportSelect.dbml?&DB_OEM_ID=1700&SPID=611&SPSID=10699',
		'UNC' : 'http://www.goheels.com/SportSelect.dbml?SITE=UNC&DB_OEM_ID=3350&SPID=12970&SPSID=668166', 'Tennessee' : 'http://www.utsports.com/sports/c-swim/sched/', 'South Carolina' : 'http://www.gamecocksonline.com/sports/c-swim/sched/scar-c-swim-sched.html',
		'VT' : 'http://www.hokiesports.com/swimming/schedule/', 'Notre Dame' : 'http://www.und.com/sports/w-swim/sched/nd-w-swim-sched.html', 'Virginia' : 'http://www.virginiasports.com/sports/c-swim/sched/va-c-swim-sched.html'
		}
		
class Event :
	def __init__(self,  date, opponent, location, time):
		self.opponent=opponent
		self.date=date
		self.location=location
		self.time=time
	def __str__(self):
		return "%s \t,  %s \t,  %s \t,  %s" % (self.opponent, self.date,self.location,self.time)


def kmpFirstMatch(pattern, hits):
	shift = computeShifts(pattern)
	startPos = 0
	matchLen = 0
	for text in hits:
		for c in text['url']:
			while matchLen >= 0 and pattern[matchLen] != c:
				startPos += shift[matchLen]
				matchLen -= shift[matchLen]
			matchLen += 1
			if matchLen == len(pattern):
				return text['url']
	return None
def computeShifts(pattern):
	shifts = [None] * (len(pattern) + 1)
	shift = 1
	for pos in range(len(pattern) + 1):
		while shift < pos and pattern[pos-1] != pattern[pos-shift-1]:
			shift += shifts[pos-shift-1]
		shifts[pos] = shift
	return shifts
	
	
def buildSchedule(input1):
	#get conference (default to AAC to avoid doing stuff)
	c= Conference.objects.get(name='AAC')
	#get or create team
	input1= input1.encode('ascii','ignore')
	t, created= Team.objects.get_or_create(name= input1, gender= 'M', conference=c)
	if created==False:
		t.save()
	#input1 = input1+(' Men Swimming & diving')
	#query = urllib.parse.urlencode({'q': input1})
	#url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
	#search_response = urllib.request.urlopen(url)
	#search_results = search_response.read().decode("utf8")
	#results = json.loads(search_results)
	#data = results['responseData']
	#hits = data['results']
	r = requests.get(list[input1])
	if r==None:
		return false
	else :
		soup = BeautifulSoup(r.text,'html.parser')
		counter =0 	
		structure=[]
	
		for td in soup.select("#schedtable > tr > td"):
			if counter < 4:
				structure.append((td.text))
				counter=counter+1
		
	
		temp=[]
		events=[]
		counter=0
	
		for td in soup.select("#schedtable > tr > td"):
			if td.get('class')!=None:	
				if td.get('class')[0]=="row-text" and counter ==4:
					e1=Event(temp[0],temp[1],temp[2],temp[3])
					events.append(e1)
					counter=0
					del temp[:]
				if counter<4 and td.get('class')[0]=="row-text":
					temp.append(td.text)
					counter=counter+1
					
		for event in events: 
				
			#check if meet exists, if not create it
			if Meet.objects.filter(name= event.opponent).count() == 0 :
				e = Meet.objects.create(name = event.opponent, gender='M', city = event.location, state=event.location, date='1900-01-01')
			else :
				e = Meet.objects.get(name=event.opponent)
			e.teams.add(t)
			e.save()