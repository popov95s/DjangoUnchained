import requests
import re 
from collections import defaultdict
from bs4 import BeautifulSoup
import json
import urllib.request, urllib.parse
from .models import Meet


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
	
	
def buildSchedule(input1)
	input1 = input1+('Swimming & diving')
	query = urllib.parse.urlencode({'q': input1})
	url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
	search_response = urllib.request.urlopen(url)
	search_results = search_response.read().decode("utf8")
	results = json.loads(search_results)
	data = results['responseData']
	hits = data['results']
	
	r = requests.get(kmpFirstMatch("sched",hits))
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
		