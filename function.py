def greeting(name):
	print ("Hello" + name)
greeting('Lucy')

#return statement  thta can be stored as a variable\
def add_num(num1,num2):
	return num1+num2
x = add_num('one' , ' two')
print(x)

#check if a number is prime
def is_prime(num):
	"""
	Input:A number
	Output: A print statement whether or not the number is prime
	"""
	for n in range(2,num):
		if num % n == 0:
			print('Not Prime ')	
		break
		
	else:
		print('Prime Number')
	
is_prime(5)
	
