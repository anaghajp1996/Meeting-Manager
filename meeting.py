class MeetingManager(object):
	

	def __init__(self,dictionary_name,dictionary_name2):
		self.available=dictionary_name
		#self.input=user_input
		self.scheduled=dictionary_name2


	def time_view(self,dictionary_name):
		for key,value in self.available.items():
			print(key,value)

	def schedule(self,dictionary_name,dictionary_name2):
		j=1
		for key,value in self.available.items():
			print(key,value)

		key_select=(input("Enter your preferred time slot: "))
		for key,value in self.available.items():
			if key==key_select:
				
				self.scheduled[j]=value

		del self.available[key_select]

		for key,value in self.scheduled.items():
			j += 1
			print(key,value)
		
		
	