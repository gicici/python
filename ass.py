#volume of a sphere
def volum(rad):
	pi = 3.14
	return 4/3 * pi * rad
print(volum(7))

def is_range(num,low,high):
	if num in range(low, high):
		print(" %s is in the range" %str(num))
	else:
		print("Number out of range")
print(is_range(5,6,9))



def s_range(num,low,high):
	return num in range(low,high)
print(is_range(3,6,9))

def is_string(s):
	dic = {"upper" : 0 , "lower" : 0}
	for i in s:
		if i.isupper():
			dic["upper"] +=1
		elif i.islower():
			dic["lower"] +=1
		else:
			pass
			print("original string", s)
			print("No of upper cases", dic["upper"])
			print("No of lower cases", dic["lower"])
			s = 'Hello Mr. Rogers, how are you this fine Sinday?'
			print(is_string(s))


def unique_list(l):
	lst =set(l)
	return lst
print(unique_list([1,1,1,1,2,2,2,3,3,3,4,5]))
#or
def unique_list(l):
	x = []
	for a in l:
		if a not in x:
			x.append(a)
			return x
print(unique_list([1,1,1,1,2,2,2,3,3,3,4,5]))


def multiply(numbers):
	total= numbers[0]
	for i in numbers:
		total*= i
		return total
print(multiply([1,2,3,-4]))

def palindrome(s):
	for i in s:
		if s == s[::-1]:
			return "Word is palindrome"
		else:
			return "Word is not"
print(palindrome("helleh"))


import string
def is_pangram(str1, alphabet= string.ascii_lowercase):
	alpa = set(alphabet)
	return alpa <= set(str1.lower())
print(is_pangram("The quick brown fox jumps over the lazy dog"))


