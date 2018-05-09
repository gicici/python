x = range(0,10)
for num in range(0,10):
	print(num)
start = 5
stop = 20
print(range(start,stop,2))

cel =[0,10,20.2,34.5]

fer =[(temp*(9/5)+ 32) for temp in cel]
print(fer)

#netsed list comprehesion
lst = [x**2 for x in[x**2 for x in range(0,10)]]#this is to the power 4
print(lst)
st = "Print only words that start with s in this sentence"
for word in st.split():
	if word[0] == 's':
		print(word)

#range for even numbers
for number in range(0,10):
	if number % 2 ==0:
		print(number)

lst=[ x for x in range(1,50) if x % 3 ==0]
print(lst)

st = 'Print only words that start with s in this sentence'
for word in st.split():
	if len(word) % 2 == 0:
		print(word + "< the word has an even length")
#fizz buzz
for number in range(0,101):
	if number % 3 == 0:
		print("Fizz")
	elif number % 5 ==0:
		print("Buzz")
	else:
		print("FizzBuzz")
st = 'Create a list of the first letters of every word in this string'
letter = [first[0] for first in st.split()]
print(letter)