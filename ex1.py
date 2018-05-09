#print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print("I'd much rather you 'not'.")
print('I "said" do not touch this. ')
#2<>1 means that 2 is not equals to one
1< 2 and 2 < 3
#the and checks if two statements are true
#count returns how many times a value appears in a code
def name_of_function(arg1,arg2):
	print (arg1+arg2)
name_of_function(1,2)
def num_prime(num):
	for n in range(2,num):
		if num % n== 0:
			print("the number is  not prime")
			break
		else:
			print("the number is prime")
num_prime(5)
def square(num):
	result = num**2
	return result
#lambda expression making an ad-hoc expression without having to rite the entire def statement
#without returnning it
lambda num: num**2
#check anumber is even
lambda num: num % 2 == 0
#first character of a string
lambda word : word[0]
#reverse a string
lambda w : w[::-1]
# taking two arguments
lambda x,y : x+y # it is not saves as a variable but it is used together with map(), filter(),reduce()


#nested Statements
#once you create a variable name in python the name is stored in a namespace
#variables have  scope and it determines the visibility of the variable name to other parts of your code
#global is outside the function
#local inside a function
#enclosing function is the one declared inside another function
#built in function are like the len()
#telling python that this is a global function
x = 50
def fun():
	global x
	print('This function is now using the global x')
	print('Becaues of global x is:' ,x)
	x =2
	print('fun(), changed global x to' , x)
print('Before calling fun(), x is:', x)
fun()
print('Value of x (outside of the fun()) is:', x)






