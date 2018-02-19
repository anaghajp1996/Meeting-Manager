from meeting import MeetingManager
schedule1={'1':"10am to 11am",'2':"11:15am to 12:15pm",'3':"2pm to 3pm"}
manage1={}


mylist=MeetingManager(schedule1,manage1) 


while True:
	key=eval(input("What would you like to do?\n\
		1.Check availabilities\n\
		2.Schedule a meeting\n\
		3.Exit:  "))
		


	if key==1:
		mylist.time_view(schedule1)

	elif key==2:

		mylist.schedule(schedule1,manage1)

	else:
		break





