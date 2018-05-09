print("I could have code like this") #and the comment after
#You can also use a comment to "disable" or comment out
#print("This wont run")
l = [1,2,3]
print(l.append(4))
#objects are things on the real world
print(l.count(3))#this is used to check the type while count()is used to 'count ' the number of times something appears.
#class is a blueprint that defines the nature of an object.blueprint means an operational plan for.
#instance is a specific object created from particular class
#attribute is a characteristic of an object
#insatnce of a class is as follows
# x = Sample()
#method is the operation we perform on an object
class Dog(object):
	#class object attribute this means no matter what object you make the species variable ill never change
	species = 'mammal'
	legs = 4
	def __init__(self, breed, name, color):
		self.breed = breed
		self.name = name
		self.color = color
sam = Dog(breed = 'Lab',name = 'Lance', color= 'brown')
print(sam.legs)# doesn't use () because it is not a method but it is an attribute
#methods are used in the encapsulation that is dividing responsilility
class Circle(object):
	pi = 3.14
	def __init__(self,radius):
		self.radius = radius
		
	def area(self):
	    return self.radius**2 * Circle.pi# we are taking it from the main class hence do not need to use self and uses self. radius to refer to the previous radius declared

	#setting a new radius
	def set_radius(self,new_radius):
		#this method takes in the current radius and resets the current radius of the Circle
		self.radius = new_radius
	def get_radius(self):
		return self.radius
	def perimeter(self):
		return self.radius * 2 * Circle.pi

c = Circle(radius = 3.4)
c.set_radius(20)
print(c.perimeter())
#inheritance is a way to form new classes from classes that have already been defined.
#derived classes are formeed from base classes.
class Animal(object):


	def __init__(self):
		print('Animal Created')

	def whoAmI(self):
		print('Animal')
	def eat(self):
		print('Eating')
class Dog(Animal):


	def __init__(self):
		Animal.__init__(self) # this is calling from the base class
		print('Dog Created')
	def whoAmI(self):
		print('Dog')
	def bark(self):
		print('Woof!')
d = Dog()
print(d)# going to display both the dog and animal created since it has called the __init__ method on it
class Book(object):

	def __init__(self, title, author, pages):
		print('A book has been created')
		self.title = title
		self.author = author
		self.pages = pages
	def __str__(self):
		return "Title %s, Author %s, Pages %s" %(self.title, self.author, self.pages)
	def __len__(self):
		return self.pages
	def __del__(self):
		print('The book is gone')


b = Book('Python' , 'Jose' , 300)
del(b)


