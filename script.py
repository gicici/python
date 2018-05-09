skill_completed = "Python Syntax"
exercises_completed = 13
#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5
point_total = 100
point_total += exercises_completed*points_per_exercise
# I had gotten an error because of forgetting the brackets
print("I got "+str(point_total)+" points!")
#backslashes are used when youre short forming
print('This isn\'t flying, this is falling with style!')
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
"""
On line 13, assign the variable fifth_letter equal to the fifth letter of the string "MONTY".

Remember that the fifth letter is not at index 5. Start counting your indices from zero.
"""
fifth_letter = "MONTY"[4]

print (fifth_letter)

string_1 = "Camelot"
string_2 = "place"
#the code below displays variable strings named above respectively  %s means cobining a string with a variable.
print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))
#i got an error because i seperated the two.
from datetime import datetime
now = datetime.now()

print ('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
menu = {} #this is an empty dictionary
kale =[] #this is an empty list
#adding a new dictionary is done as follows and adiing key value to the pair
menu ['Fried Rice'] = 50.34
#deleting dictionaries is done as follows
del dict_name[key_name]
#adding key value is done as follows
dict_name[key] = new_value
#deleting from list is as follows
list_name.remove('string')




inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
#got an error because of the append method
inventory['gold'] = inventory['gold'] + 50


#for loop
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names:
  print (name)

#for loop for keys
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for key in webster:
  print webster[key]


#Checking divisisbility
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# please do not forget to call the number after 2
for number in a:
  if number % 2 == 0:
    print (number)
 # this is a function
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return (count)



  total = 0
for food in prices:
  print (prices[food] * stock[food])
  total = total + prices[food] * stock[food]
print (total)





def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  
  total = homework *.1 + quizzes * .3 + tests * .6
  return total



  # range loop is as follows giving an example
  for i in range (len(n)):
  	print n[i]

