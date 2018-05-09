if True:
	print('It is True')



x = 'False'
if x:
	print('x was True')
else:
	print('I will print when x is false')



loc = 'Bank'
if loc == 'Auto Shop':
	print ('Welcome to the Auto Shop')
elif loc == 'Bank':
	print ('Welcome to the bank')
else:
	print ('Youre lost')



person = 'sam'
if person == 'sam':
	print('Hi sam')
else:
	print("What's your name?")# use double quotations if you want use an apostrophe



print('Lucy {x} , Njoki {y}'.format(x ='First name' , y='Second name'))
#for loop
l = [1,2,3,4,5]
for element in l:
	print(element)
for element in l:
	print("something")
#since the list above the word print something will be iterated five times.
#to iterate mena sto repeat something over and over
#modulo uses to get a remainder of something and displays the reminder
#eg 10 %3 it will display one
#to find a number has a even
num = [2,3,4,5]
for number in num:
	if number % 2 == 0 :
		print('number')
	else:
		print('THis is an odd number')
	
list_sum = 0
for num in l:
	list_sum = list_sum + num
print(list_sum)

s = "This is a string"
for letter in s:
	print(letter)

#for loop in a tuple
tup =(1,2,3,4,5)
for t in tup:
	print(t)
#tuple unpacking
l =[(2,4),(6,8),(10,42)]
for tup in l:
	print(tup)

for (t1,t2) in l:
	print(t1)#this is tuple unpacking ie getting elements in the first pack of the tuple




dic = {'k1': 'Lucy', 'k2' : 'Njoki', 'k3': 'Gicici'}
for item in dic:
	print(item)#it is going to display only the keys


#pyhton 2 to iterate in a dictionary you will use .iteritems() and .items() iin pyhton 3
for k, v in dic.items():
	print (k)
	print (v)
# find the largest of three numbers
n =[20,40,50]
print(max(n)) 
#while loop will execute till a true value occurs
x = 0
while x < 10:
	print('x is currently ', x)
	x +=1
else:
	print('All done')
#break means it stops where the code has it and it does't execute the rest of the code
#continue Goes to the top of the closest enclosing loop
#pass does nothing at all
x = 0
while x < 10:
	print('x is currently',x)
	print('X is still less than 10, adding 1 to x')
	x +=1
	if x == 3:
		print('Hey x equals 3')
		break
	else:
		print('Continuing....')
		continue
	#while True: print('Infinite') the code will exucte infinitetly meaning it doesn't end
	#range helps you to identify a list from a starting point to an ending point
range(10)
x = range(10)
print(x)
print(type(x))	
start = 0
stop = 20
print(start, stop, 3) # the third is the step size that goes by three
l =[1,2,3,4,5]
for num in range(1,7):#xrange is used inpython three while range function is used in pyhton 2
	print(num)
#list comprehesion allows us to build out lists using different notations
l =[]
for letter in "Word":
	l.append(letter)
print(l)

#list compreheison starts here
l =[letter for letter in "Word"]
x = [number**2 for number in range(0,10)]
print(x)
#even numbers in a range
y =[num for num in range(15,30)if num %2 == 0]
print(y)
lst= []
for num in range(0,10):
	if num %2 == 0:
		print(lst.append(num))
#checking if a word is isogram
def is_isogram(word):
	l = set(word)
	lu = [ a for a in l]
	if len(l) == len(lu):
		return True
		return False
is_isogram("George")
