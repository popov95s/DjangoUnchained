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
	conference = models.ForeignKey(Conference, on_delete= models.SET_DEFAULT,default= "")

	gender = models.CharField(choices=GENDERS, max_length=1, default="")			#should not be default = "" but it wants a default since rows already exist

	#possibly something about facilities

class Event(models.Model):
	EVENTS = (
		("Free","Freestyle"),
		("Back","Backstroke"),
		("Breast","Breaststroke"),
		("Fly", "Butterfly"),
		("IM", "Individual Medley")
	)
	#DISTANCES= (
	#	50,100,200,400,500,800,1000,1500,1650
	#)
	COURSES = (
		("SCY", "Short Course Yards"),
		("SCM", "Short Course Meters"),
		("LCM", "Long Course Meters")
	)
	#needs logic for distances and events to make sure there's no 1650LCM Fly
	event = models.CharField(choices=EVENTS,max_length=10)
	#distance = models.IntegerField(choices=DISTANCES)
	course = models.CharField(choices=COURSES, max_length=3)
	

class Swimmer(models.Model):
	name = models.CharField(max_length=255)
	date_of_birth = models.DateField(blank=True,default= "")
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

	#login info for registered users 
	email = models.CharField(unique=True, blank=True, max_length=40, default="")
	password_hash= models.CharField(blank=True, default="", max_length=255)
	salt = models.CharField(blank=True, default="", max_length=10)
	registration_date= models.DateField(blank=True, null=True)


class Meet(models.Model):
	GENDERS = (
		("M", "Men"),
		("W", "Women")
	)
	STATUSES =  (
		("C","Completed"), ("I","In Progress"), ("N","Not started")
	)
	name = models.CharField(max_length=255)
	teams = models.ManyToManyField(Team)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	date = models.DateField()
	gender = models.CharField(choices=GENDERS, max_length=1)
	status = models.CharField(choices=STATUSES, max_length=1)
	


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
	place = models.PositiveIntegerField()											#what place did the swimmer get in the event
	points = models.PositiveIntegerField()											#how many points did he earn for his team
	event = models.ForeignKey(Event)
	time_type= models.CharField(choices= TYPES, max_length=11, default="Final") 	#setting default to Final ( as in Timed Final )
