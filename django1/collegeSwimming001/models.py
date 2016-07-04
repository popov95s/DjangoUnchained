from django.db import models


class Division (models.Model):
	name= models.CharField(max_length=255)


class Conference(models.Model):
	name= models.CharField(max_length=255)
	division = models.ForeignKey(Division)
	

class Team(models.Model):
	GENDERS = (
		("M", "Men"),
		("W", "Women")
	)
	name = models.CharField(max_length=255)											#not sure if this should make Meet.gender redundant
	abbreviation = models.CharField(max_length=16, default= "")
	conference = models.ForeignKey(Conference, on_delete= models.SET_DEFAULT,default= "")
	gender = models.CharField(choices=GENDERS, max_length=1, default="")			#should not be default = "" but it wants a default since rows already exist
	city = models.CharField(blank=True, default ="",max_length=255)
	state =models.CharField(blank=True, default="", max_length=2)
	
	#possibly something about facilities
	def __str__(self):
		str = "%s \t,  %s \t,  %s \t,  %s  \t,  %s   \t,   %s  \n " % (self.name, self.abbreviation,self.city, self.state, self.gender,self.conference.name)
		return str

class Event(models.Model):
	EVENTS = (
		("1","Freestyle"),
		("2","Backstroke"),
		("3","Breaststroke"),
		("4", "Butterfly"),
		("5", "Individual Medley")
	)
	COURSES = (
		("SCY", "Short Course Yards"),
		("SCM", "Short Course Meters"),
		("LCM", "Long Course Meters")
	)
	#needs logic for distances and events to make sure there's no 1650LCM Fly
	stroke = models.CharField(choices=EVENTS,max_length=10)
	distance = models.IntegerField()
	course = models.CharField(choices=COURSES, max_length=3)
	def __str__(self):
		str = "%s \t,  %s \t,  %s \n" % (self.stroke, self.distance,self.course)
		return str
	

class Swimmer(models.Model):

	GENDERS = (
		("M", "Men"),
		("W", "Women")
	)
	
	name = models.CharField(max_length=255)
	date_of_birth = models.DateField()
	gender = models.CharField(choices=GENDERS, max_length=1, default="")
	teams = models.ManyToManyField(Team)
	grad_year = models.DateField() 													#only using year here
	city = models.CharField(blank=True, default ="",max_length=255)
	state =models.CharField(blank=True, default="", max_length=2)
	country = models.CharField(blank=True, default="", max_length=255) 				#should be a choices= ...
	zipcode= models.CharField(max_length=5,blank=True,default="")
	home_phone= models.CharField(blank=True, default="",max_length=10)
	facebook= models.CharField(blank=True,default="", max_length=255)
	twitter	= models.CharField(blank=True,default="", max_length=255)
	# + a lot more personal info 

	#login info for registered users should be in a separate table
	#email = models.CharField(unique=True, blank=True, max_length=40, default="")
	#password_hash= models.CharField(blank=True, default="", max_length=255)
	#salt = models.CharField(blank=True, default="", max_length=10)
	#registration_date= models.DateField(blank=True, null=True)
	def __str__(self):
		str = "%s \t,  %s \t,  %s \t,  %s  \t,  %s   \t,  \n Teams: " % (self.name, self.date_of_birth,self.city, self.state, self.gender)
		for team in self.teams.all() : 
			str+= team.name
		return str

class Meet(models.Model):
	STATUSES =  (
		("C","Completed"), ("I","In Progress"), ("N","Not started")
	)
	name = models.CharField(max_length=255)
	teams = models.ManyToManyField(Team)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	startDate = models.DateField()
	endDate = models.DateField()
	status = models.CharField(choices=STATUSES, max_length=1, default="N")
	def __str__(self):
		str = "%s \t,  %s \t,  %s \t,  %s  \t,  %s   \t,   %s  \n Teams: " % (self.name, self.city,self.state, self.status, self.startDate,self.endDate)
		for team in self.teams.all() : 
			str+= team.name
		return str

class Coaches(models.Model):
	name= models.CharField(max_length=255)
	role = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	team = models.ForeignKey(Team, on_delete=models.SET_DEFAULT, default="")		#assuming same logic as when deleting the team 
																					#(unless email gets changed when moving teams )




#maybe should have a separate one just for relay times
#not handling splits, maybe should be separate class with one-to-many relationship to Time
class Time(models.Model):

	TYPES = (
		("Prelim","Preliminary"),
		("Semi", "Semi-Final"),
		("Final", "Final"),
		("Swim-Off","Swim-Off"),
		("Time trial","Time trial")
	)

	swimmer = models.ForeignKey(Swimmer, default ="") 								#foreign key to reference 1 swimmer
	time = models.CharField(max_length=8) 											#should be mm:ss.hh, can't find something suitable
	meet= models.ForeignKey(Meet, on_delete = models.CASCADE)						#can only belong to single meet
	place = models.PositiveIntegerField(default= 0)									#what place did the swimmer get in the event
	points = models.PositiveIntegerField(default=0)									#how many points did he earn for his team
	event = models.ForeignKey(Event)
	time_type= models.CharField(choices= TYPES, max_length=11, default="Final") 	#setting default to Final ( as in Timed Final )
	team = models.ForeignKey(Team, default="")										#FK to reference 1 team

	def __str__(self):
		str = "%s \t,  %s \t,  %s \t,  %s  \t,  %s   \t,   %s  \n " % (self.swimmer.name, self.time,self.meet.name, self.place, self.points,self.event.stroke)
		return str
#Relay time is a separate class used just for relays
class RelayTime(models.Model):
	lead_off= models.ForeignKey(Time,default="",related_name="lead_off")			#lead off 
	legs = models.ManyToManyField(Time, related_name="legs")						#all other swimmers in that relay
