class Animal():
	name = "Amy"
	noise = "Grunt"
	size = "Large"
	color = "brown"
	hair = 'Covers body'
	def get_color(self):
		return self.color
	def make_noise(self):
		return self.noise

dog = Animal()
dog.make_noise()
dog.size = "small"
dog.color = "black"
dog.hair = "hairless"

class Dog(Animal):
	name = 'Omar'
	size = "small"
	color = "black"
	age = 19

omar = Dog()
omar.color = 'white'
omar.name = 'Omar Agely'
