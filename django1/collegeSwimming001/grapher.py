
from collegeSwimming001.models import Swimmer,Time
import math
import requests
import heapq
import pprint

#base times used are a .05% faster than US open records as of 2015. These are only male times
baseTimes = [18.38,40.56,90.74,247.30,513.91,859.20,43.85,96.29,49.79,108.12,43.96,98.81,98.88,213.43]


#converts a string time to float 
def convertTime(times):
	for event, time in times.items():
		if ':' in time: 
			if time.index(':')==1:
				time = float(time[0])*60 + float(time[2:4]) + 0.01*float(time[5:7])
			if time.index(':')==2:
				time= float(time[0:2])*60 + float(time[3:5]) + 0.01*float(time[6:7])
		else:
			time =  float(time[0:time.index('.')]) + 0.01*float(time[time.index('.')+1:5])


#converts a time from float to MM:SS.HH format
def convertMinutesToSeconds(times):
	for time in times:
		if float(time['eventtime'])/60 < 1 :
			time['eventtime'] =  str(float(time['eventtime'])%60)
		else:
			if (float(time['eventtime'])%60 >10.0): 
				time['eventtime'] = str(int(float(time['eventtime'])/60)) + ":"+ str(float(time['eventtime'])%60) 
			elif (float(time['eventtime'])%60 <10.0): 
				time['eventtime'] = str(int(float(time['eventtime'])/60)) + ":0"+ str(float(time['eventtime'])%60) 

#returns a tuple of event and points for that event
def getPointsAndEvent(timeEntry):
	return [( timeEntry['eventstroke'] , (str(timeEntry['eventdistance']))+timeEntry['eventcourse']), timeEntry['pointvalue']]


#returns a tuple of event and time for that event
def getTimeAndEvent(timeEntry):
	return {'eventstroke': timeEntry['eventstroke'], 'eventdistance' :timeEntry['eventdistance'], 'eventcourse': timeEntry['eventcourse'], 'meet':timeEntry['meet'], 'eventtime':timeEntry['eventtime'], 'pointvalue':timeEntry['pointvalue'] }
	#return [( timeEntry['eventstroke'] , (str(timeEntry['eventdistance']))+timeEntry['eventcourse']), (timeEntry['eventtime'], timeEntry['meet'])]

# return points if they exist, else returns 0.0
def getPointsIfExists(event_stroke,event_distance, scores):
	if (str(event_stroke),str(event_distance)) in scores:
		return float((scores[(event_stroke,event_distance)]))
	else :
		return 0.0

#returns time if itexists else returns None
def getTimeIfExists(event_stroke,event_distance, times):
	if (str(event_stroke),str(event_distance)) in times:
		return (times[(event_stroke,event_distance)])
	else :
		return None

# returns two best points from an array
def getTwoBestPoints(scores):
	return heapq.nlargest(2, scores)


#return Distance ratio calculated by sprint, mid and distance points out of 100
def getDistanceRatio(sprint, mid, distance):
	total = sprint+mid + distance*2
	if total > 0.0:
		return {'sprint': sprint/total, 'mid' : mid/total, 'distance': distance*2/total }
	else:
		return None




#get best time by points
def getTimeByEvent(maxPoints, scores, times, stroke):
	for event in scores:
		for time in times :
			if time['eventstroke'] == stroke and float(time['pointvalue'])==float(maxPoints):
				return time
	return {}


#takes scores in each event and returns a score for Sprint, Distance, Back, Breast,Fly
def calculateScores(swimmerID):
	#cookie to connect to API
	cookie = {'_ga':'GA1.2.1860246398.1464211181', '_cb_ls':'1', '_chartbeat2' : '.1464211187032.1470951297630.1000010000000001', '_cb':'Css_k6CSd27eDbaWFi', 'csrftoken':'hytYr7YxmUGB4NoTJAc0hPEFXLfOZHno', 'gender':'M', 'sessionid':'y5b8a6eriai0t9mdlk7x5yb64lnvy695', 'region_id':'division-1', 'collegeteam_id':'75'}
	r= requests.get('https://www.collegeswimming.com/api/swimmers/'+str(swimmerID)+'/records/',cookies = cookie)

	#scores 
	scr= dict(map(getPointsAndEvent,r.json()))
	
	#times
	times = list(map(getTimeAndEvent,r.json()))
	
	#points for each event
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

	#points for each stroke
	freePoints= [fiftyFreePoints, oneFreePoints, twoFreePoints, fiveFreePoints, tenFreePoints, milePoints]
	backPoints = [oneBackPoints, twoBackPoints]
	breastPoints = [oneBreastPoints, twoBreastPoints]
	flyPoints = [oneFlyPoints, twoFlyPoints]
	IMPoints = [twoIMPoints, fourIMPoints]
	

	#sprint, mid, distance events split up
	sprintEvents = [fiftyFreePoints, oneFreePoints, oneBackPoints, oneBreastPoints, oneFlyPoints]
	midEvents = [twoFreePoints, fiveFreePoints, twoBackPoints, twoBreastPoints, twoFlyPoints, twoIMPoints, fourIMPoints]
	distanceEvents = [tenFreePoints, milePoints]

	#scores for each
	sprintScore = (getTwoBestPoints(sprintEvents)[0]+ getTwoBestPoints(sprintEvents)[1])
	midScore = (getTwoBestPoints(midEvents)[0]+ getTwoBestPoints(midEvents)[1])
	distanceScore = (getTwoBestPoints(distanceEvents)[0])
	
	#get ratio
	ratio = getDistanceRatio(sprintScore,midScore,distanceScore)
	ratio = ratio['mid']*500 + ratio['distance']*1000




	#scores for each stroke
	freeScore = (getTwoBestPoints(freePoints)[0] + 0.2*getTwoBestPoints(freePoints)[1])/1.2	
	backScore = (getTwoBestPoints(backPoints)[0] + 0.2*getTwoBestPoints(backPoints)[1])/1.2
	breastScore = (getTwoBestPoints(breastPoints)[0] + 0.2*getTwoBestPoints(breastPoints)[1])/1.2
	flyScore = (getTwoBestPoints(flyPoints)[0] + 0.2*getTwoBestPoints(flyPoints)[1])/1.2
	IMScore = (getTwoBestPoints(IMPoints)[0] + 0.2*getTwoBestPoints(IMPoints)[1])/1.2
		
	#scores for each distance (not used anymore)
	sprintFreeScore = (fiftyFreePoints + oneFreePoints)/2
	midFreeScore = (twoFreePoints + fiveFreePoints)/2
	distanceFreeScore=(milePoints)



	#convert to ease 
	convertMinutesToSeconds(times) 

	#get best time by stroke
	bestFreeTime = getTimeByEvent(getTwoBestPoints(freePoints)[0], scr, times,'1')
	bestBackTime = getTimeByEvent(getTwoBestPoints(backPoints)[0], scr, times,'2')
	bestBreastTime = getTimeByEvent(getTwoBestPoints(breastPoints)[0], scr, times,'3')
	bestFlyTime = getTimeByEvent(getTwoBestPoints(flyPoints)[0], scr, times,'4')
	bestIMTime = getTimeByEvent(getTwoBestPoints(IMPoints)[0], scr, times, '5')
	bestTimes = (bestFreeTime ,  bestBackTime ,  bestBreastTime , bestFlyTime , bestIMTime)
	
	#json to return
	scores = {	"Free" : round(freeScore,2),"Back": round(backScore,2), "Breast" : round(breastScore,2), "Fly" : round(flyScore,2), 
				"IM" : round(IMScore,2),"Distance" : round(ratio,2), 'times' : bestTimes} 
	return scores
	
	
	