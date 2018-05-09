my_list=[1,2,3]
print(my_list)
#Lists can hold different types of numbers, strings or even floating point numbers
my_list= ['string',1,0.3,67, 'o']
print(my_list)
#len stands foor length
print(len(my_list))
my_list = ['one','two', 'three', 4,5]
#grabs elements on the index and that is 1 
print(my_list[0])
l = [1,4,5]
l.append('append')
#append method above is used to add items permanetly to a list
print(l)
#nesting lists
lst_1 = [4,5,9]
lst_2 = [2,7.0]
lst_3 = [1,3,6]
matrix = [lst_1,lst_2,lst_3]
print(matrix)
my_list[4] = (4,5,8)
print(my_list )
l = []
for letter in l:
	l.append(letter)
	print(l)

l = [letter for letter in 'word']


lst = [number for number in range(11) if number%2==0]
print(lst)

celsius = [ 0,10,20.1,34.5]
fahrenheit = [ temp  for temp in celsius]
print(fahrenheit)
lst = [x**2 for x in[x**2 for x in range(11)]]
print(lst)