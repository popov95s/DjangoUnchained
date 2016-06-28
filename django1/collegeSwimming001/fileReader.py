import re

from collegeSwimming001.models import Team, Meet, Event, Time, Conference

def fixDate(date):
	date = date[4:8] + '-' + date[0:2] + '-' + date[2:4]
	return date

meetFile = file(r'C:\Users\Stefan Popov\Documents\django1\django1\collegeSwimming001\57225.cl2').read()


#meet and team objects used 
m, t=""


c = Conference.objects.filter(name='AAC').first()


for line in meetFile.split('\n'):

	if line[0:2] == 'A0':
		#don't care about this rn
		continue
	
	elif line[0:2]== 'B1':
		#get meet name
		meetName = line[11:42].strip(' ')
		meetCity = line[85:105].strip(' ')
		meetState = line[105:107].strip(' ')
		meetCountry = line[117:120].strip(' ')
		meetStartDate = line[121:129].strip(' ')
		meetEndDate= line[129:137].strip(' ')
		meetCourse = line[149:150].strip(' ')
		meetStartDate= fixDate(meetStartDate)
		meetEndDate= fixDate(meetEndDate)
		m = Meet(name = meetName, city = meetCity, state = meetState, startDate= meetStartDate, endDate= meetEndDate, status= 'C')
		
		print meetName +  '\n' + meetCity + '\n' + meetState  + '\n' + meetCountry + '\n' + meetStartDate + '\n' + meetEndDate + '\n' + meetCourse + '\n'
		m.save()
		
		
	elif line[0:2]== 'C1':
		currentTeam = line[17:47].strip(' ')
		teamAbbreviation = line[47:63].strip(' ')
		teamCity = line[107:127].strip(' ')
		teamState = line[127:129].strip(' ')
		#default conference to AAC for simplicity and gender to M 
		# TODO : should teams have genders, since it can't be taken from meet results
		t = Team(name = currentTeam, abbreviation=teamAbbreviation, city= teamCity, state= teamState, conference=c, gender = 'M')
		
		t.save()
		#blows up stack
		m.teams.add(t)
		print currentTeam + '\n' + teamAbbreviation + '\n' + teamCity + '\n' + teamState
	elif line[0:2]== 'D0':
		swimmerName= line[11:39].strip(' ')
		swimmerBirthDate = line[55:63].strip(' ')
		swimmerSex = line[65:66].strip(' ')
		eventDistance = line[67:71].strip(' ')
		eventStroke = line[71:72]
		eventTime= line[115:123]
		print swimmerName + '\t\t' + swimmerBirthDate + '\t\t' + swimmerSex + '\t\t' + eventDistance + '\t\t' + eventStroke + '\t' + eventTime
	#elif line[0:2]== 'E0':
	
	#elif line[0:2]== 'F0':
	#
	elif line[0:2]== 'Z0':
		break
