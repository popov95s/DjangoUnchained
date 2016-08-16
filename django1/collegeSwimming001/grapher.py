
from collegeSwimming001.models import Swimmer,Time
import math
import requests
import heapq
import pprint


baseTimes = [18.38,40.56,90.74,247.30,513.91,859.20,43.85,96.29,49.79,108.12,43.96,98.81,98.88,213.43]

def convertTime(times):
	for event, time in times.items():
		print time 
		if ':' in time: 
			if time.index(':')==1:
				time = float(time[0])*60 + float(time[2:4]) + 0.01*float(time[5:7])
			if time.index(':')==2:
				time= float(time[0:2])*60 + float(time[3:5]) + 0.01*float(time[6:7])
		else:
			time =  float(time[0:time.index('.')]) + 0.01*float(time[time.index('.')+1:5])

def convertMinutesToSeconds(times):
	for event,time in times.iteritems():
		if float(time)/60 < 1 :
			times[event] =  str(float(time)%60) 
		else: 
			times[event] = str(int(float(time)/60)) + ":"+ str(float(time)%60) 

def getPointsAndEvent(timeEntry):
	return [( timeEntry['eventstroke'] , (str(timeEntry['eventdistance']))+timeEntry['eventcourse']), timeEntry['pointvalue']]

def getTimeAndEvent(timeEntry):
	return [( timeEntry['eventstroke'] , (str(timeEntry['eventdistance']))+timeEntry['eventcourse']), timeEntry['eventtime']]

def getPointsIfExists(event_stroke,event_distance, scores):
	if (str(event_stroke),str(event_distance)) in scores:
		return float((scores[(event_stroke,event_distance)]))
	else :
		return 0.0

def getTimeIfExists(event_stroke,event_distance, times):
	if (str(event_stroke),str(event_distance)) in times:
		return (times[(event_stroke,event_distance)])
	else :
		return None

def getTwoBestPoints(scores):
	return heapq.nlargest(2, scores)

def getDistanceRatio(sprint, mid, distance):
	total = sprint+mid + distance*2
	if total > 0.0:
		return {'sprint': sprint/total, 'mid' : mid/total, 'distance': distance*2/total }
	else:
		return None

#clean this !! 

def convertTimeTuples(times):
	for event, time in times.items():
		times[str(event[0])+str(event[1])]= time
		times.pop(event,time)


#takes scores in each event and returns a score for Sprint, Distance, Back, Breast,Fly
def calculateScores(swimmerID):
	#swimmerTimes = Time.objects.filter(swimmer=swimmerID)
	#
	##get all times 
	#fiftyFreeTime = convertTime(swimmerTimes.filter(event__stroke='1').filter(event__distance=50).order_by('time').first())
	#oneFreeTime = convertTime(swimmerTimes.filter(event__stroke='1').filter(event__distance=100).order_by('time').first())
	#twoFreeTime= convertTime(swimmerTimes.filter(event__stroke='1').filter(event__distance=200).order_by('time').first())
	#fiveFreeTime = convertTime(swimmerTimes.filter(event__stroke='1').filter(event__distance=500).order_by('time').first())
	#tenFreeTime = convertTime(swimmerTimes.filter(event__stroke='1').filter(event__distance=1000).order_by('time').first())
	#mileTime = convertTime(swimmerTimes.filter(event__stroke='1').filter(event__distance=1650).order_by('time').first())
	#oneBackTime = convertTime(swimmerTimes.filter(event__stroke='2').filter(event__distance=100).order_by('time').first())
	#twoBackTime= convertTime(swimmerTimes.filter(event__stroke='2').filter(event__distance=200).order_by('time').first())
	#oneBreastTime = convertTime(swimmerTimes.filter(event__stroke='3').filter(event__distance=100).order_by('time').first())
	#twoBreastTime = convertTime(swimmerTimes.filter(event__stroke='3').filter(event__distance=200).order_by('time').first())
	#oneFlyTime= convertTime(swimmerTimes.filter(event__stroke='4').filter(event__distance=100).order_by('time').first())
	#twoFlyTime= convertTime(swimmerTimes.filter(event__stroke='4').filter(event__distance=200).order_by('time').first())
	#twoIMTime= convertTime(swimmerTimes.filter(event__stroke='5').filter(event__distance=200).order_by('time').first())	
	#fourIMTime= convertTime(swimmerTimes.filter(event__stroke='5').filter(event__distance=400).order_by('time').first())
	#
	cookie = {'_ga':'GA1.2.1860246398.1464211181', '_cb_ls':'1', '_chartbeat2' : '.1464211187032.1470951297630.1000010000000001', '_cb':'Css_k6CSd27eDbaWFi', 'csrftoken':'hytYr7YxmUGB4NoTJAc0hPEFXLfOZHno', 'gender':'M', 'sessionid':'y5b8a6eriai0t9mdlk7x5yb64lnvy695', 'region_id':'division-1', 'collegeteam_id':'75'}
	r= requests.get('https://www.collegeswimming.com/api/swimmers/'+str(swimmerID)+'/records/',cookies = cookie)

	#print r.json()
	scr= dict(map(getPointsAndEvent,r.json()))

	times = dict(map(getTimeAndEvent,r.json()))
	#print scr[('1','50Y')]
	fiftyFreePoints = getPointsIfExists('1','50Y', scr)
	oneFreePoints = getPointsIfExists('1','100Y', scr)
	twoFreePoints = getPointsIfExists('1','200Y', scr)
	fiveFreePoints = getPointsIfExists('1','500Y', scr)
	tenFreePoints = getPointsIfExists('1','1000Y', scr)
	milePoints = getPointsIfExists('1','1650Y', scr)
	oneBackPoints = getPointsIfExists('2','100Y', scr)
	twoBackPoints = getPointsIfExists('2','200Y', scr)
	oneBreastPoints = getPointsIfExists('3','100Y', scr)
	twoBreastPoints = getPointsIfExists('3','200Y', scr)
	oneFlyPoints = getPointsIfExists('4','100Y', scr)
	twoFlyPoints = getPointsIfExists('4','200Y', scr)
	twoIMPoints = getPointsIfExists('5','200Y', scr)
	fourIMPoints = getPointsIfExists('5','400Y', scr)


	
	#calculate scores
#	sprintScore = (math.pow((baseTimes[0]/fiftyFreeTime),3)*1000 + math.pow((baseTimes[1]/oneFreeTime),3)*1000 + math.pow((baseTimes[2]/twoFreeTime),3)*1000 + math.pow((baseTimes[3]/fiveFreeTime),3)*1000 + math.pow((baseTimes[4]/tenFreeTime),3)*1000 + math.pow((baseTimes[5]/mileTime),3)*1000)/2
#	distanceScore = (math.pow((baseTimes[3]/fiveFreeTime),3)*1000 + math.pow((baseTimes[4]/tenFreeTime),3)*1000 + math.pow((baseTimes[5]/mileTime),3)*1000)/3
#	backScore = (math.pow((baseTimes[6]/oneBackTime),3)*1000 + math.pow((baseTimes[7]/twoBackTime),3)*1000)/2
#	breastScore = (math.pow((baseTimes[8]/oneBreastTime),3)*1000 + math.pow((baseTimes[9]/twoBreastTime),3)*1000)/2
#	flyScore = (math.pow((baseTimes[10]/oneFlyTime),3)*1000 + math.pow((baseTimes[11]/twoFlyTime),3)*1000)/2750
#	IMScore = (math.pow((baseTimes[12]/twoIMTime),3)*1000 + math.pow((baseTimes[13]/fourIMTime),3)*1000)/2
#	
	freePoints= [fiftyFreePoints, oneFreePoints, twoFreePoints, fiveFreePoints, tenFreePoints, milePoints]
	backPoints = [oneBackPoints, twoBackPoints]
	breastPoints = [oneBreastPoints, twoBreastPoints]
	flyPoints = [oneFlyPoints, twoFlyPoints]
	IMPoints = [twoIMPoints, fourIMPoints]
	
	sprintEvents = [fiftyFreePoints, oneFreePoints, oneBackPoints, oneBreastPoints, oneFlyPoints]
	midEvents = [twoFreePoints, fiveFreePoints, twoBackPoints, twoBreastPoints, twoFlyPoints, twoIMPoints, fourIMPoints]
	distanceEvents = [tenFreePoints, milePoints]


	sprintScore = (getTwoBestPoints(sprintEvents)[0]+ getTwoBestPoints(sprintEvents)[1])
	midScore = (getTwoBestPoints(midEvents)[0]+ getTwoBestPoints(midEvents)[1])
	distanceScore = (getTwoBestPoints(distanceEvents)[0])
	ratio = getDistanceRatio(sprintScore,midScore,distanceScore)


	ratio = ratio['mid']*500 + ratio['distance']*1000

	freeScore = (getTwoBestPoints(freePoints)[0] + 0.2*getTwoBestPoints(freePoints)[1])/1.2	
	backScore = (getTwoBestPoints(backPoints)[0] + 0.2*getTwoBestPoints(backPoints)[1])/1.2
	breastScore = (getTwoBestPoints(breastPoints)[0] + 0.2*getTwoBestPoints(breastPoints)[1])/1.2
	flyScore = (getTwoBestPoints(flyPoints)[0] + 0.2*getTwoBestPoints(flyPoints)[1])/1.2
	IMScore = (getTwoBestPoints(IMPoints)[0] + 0.2*getTwoBestPoints(IMPoints)[1])/1.2
		
	sprintFreeScore = (fiftyFreePoints + oneFreePoints)/2
	midFreeScore = (twoFreePoints + fiveFreePoints)/2
	distanceFreeScore=(milePoints)


	print times 
	convertMinutesToSeconds(times) 
	convertTimeTuples(times)
	print times



	#have times be only top times per stroke


	scores = {	"Free" : round(freeScore,2),"Back": round(backScore,2), "Breast" : round(breastScore,2), "Fly" : round(flyScore,2), 
				"IM" : round(IMScore,2),"Distance" : round(ratio,2), 'times' : times} 
	return scores
	
	
	
print calculateScores(356405)
	