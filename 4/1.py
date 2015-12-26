'''
Create a class to represent city which contains a list of places to see.
- Provide methods to create the object with just the city name or with
city name and places (stored as list)
- Provide methods to add a place of visit, to remove place of visit, to
display all places of visit.
Add exceptional handling so that remove does not crash if the given place
is not in the city
'''
class City:
	def __init__(name,places=None):
		self.name=name
		if places is None:
			self.places=list()
		else:
			self.places=places
	def add_place(self,place):
		self.places.append(place)
	def remove_place(self,place):
		try:		
			if place in self.places:
				self.places.remove(place)
		except Exception as E:
			print('Place not in places')
	def disp(self):
		print('City:',self.name)
		for i in self.places:
			print('\t',i)

