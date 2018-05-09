#class blueprint thta defines a nature of a future object
#instance is a specific object created from a class
class Sample(object):
	pass
x = Sample()
print(x)
#attribute is a characteristic of the object and a method is an operation we can perform on an object
class Dog(object):
	#class object attribute
	species = 'mammal'

	def __init__(self,breed,name,legs): #method
		self.breed = breed #attribute
		self.name = name
		self.legs = legs
sam = Dog(breed = 'Lab', name = 'Sammy', legs = '4')
print(sam.legs)
#methods help in encapsulation this helps to divide responsibilities in programming and handle large applications
class Circle(object):
	#class objectt attribute
	pi = 3.14
	def __init__(self,radius = 1):
		self.radius = radius
	def area (self):
		#radius **2 *pi
		return (self.radius **2)*Circle.pi
	def set_radius(self, new_radius):
		self.radius = new_radius
	def get_radius(self):
		return self.radius
	def perimeter(self):
		return(self.radius)*2*Circle.pi
c = Circle(radius = 200)
c.set_radius(20)	
print (c.perimeter())

#inheritanvce is a way to form new classes thta have already been defined.
#newly formed classes are called derived classes and classes derived form are called base classes
class Animal(object):

	def __init__(self):
		print(" Animal Created")
	def whoAmI(self):
		print("Animal")
	def eat(self):
		print("Eating")
class Dog (Animal):

	def __init__(self):
		Animal.__init__(self)
		print("Dog created")
	def whoAmI(self):
		print("Dog")
	def bark(self):
		print("Woof!")
d = Dog()
print(d)
#special methods
class Book(object):

	def __init__(self,title,author,pages):
		print("Book has been created")
		self.title = title
		self.author = author
		self.pages = pages
	"""
	def __str__(self):
		return "Title %s, Author %s,Pages %s"%(self.title,self.author,self.pages)
	"""
	"""
	def __len__(self):
		return self.pages
	"""
	def __del__(self):
		print("The book has been deleted")
b = Book('Python','Lucy',300)
print( (b))
