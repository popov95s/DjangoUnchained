import re

from .models import Team, Meet, Event, Time

meetFile = file("55329.cl2").read()
currentTeam = ""

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
		m = Meet(name = meetName, city = meetCity, state = meetState, startDate= meetStartDate, endDate= meetEndDate)
		print meetName +  '\n' + meetCity + '\n' + meetState  + '\n' + meetCountry + '\n' + meetStartDate + '\n' + meetEndDate + '\n' + meetCourse + '\n'
		
		
	elif line[0:2]== 'C1':
		currentTeam = line[17:47].strip(' ')
		teamAbbreviation = line[47:63].strip(' ')
		teamCity = line[107:127].strip(' ')
		teamState = line[127:129].strip(' ')
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
	