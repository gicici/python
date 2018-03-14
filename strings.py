print('Hello there this is a string')
print("don't know you")
#when writing a new line use \n
print('Here is a new line \n and here is the continuation')
print(len('Hello World'))
#the above statement shows the lenght of the string
s = "My name is Lucy"
#below is an example of indexing
print(s)
print(s[4])
#this is how slicing works grabs from the index declared till the end
print(s[1:])
#this is grabbing everything till the fourth index
print(s[:4])
#example of concentination
print(s + " Gicici")
#reassign variables
s = s + "Gicici"
print(s)
y = 'Hello'
print(y*10)
#to call method in a string is as follows
s = "Lucy Gicici"
print(s.upper())
#if you want to split you can do it as follows
print(s.split('u'))
#this is insrting another string inside
p = 'This'
print("Insert my string here: %s" %(p))
#This is cutting off floating point numbers inshort to the nearest decimal place
print("This is a floating point number %1.3f" %(13.4555))
#passing in many variables
print('First %s:, Second %s, Third %s' %('Hi','to','you'))
#formatting variables
print('First {v}: Second {v}'.format( v ="This"))