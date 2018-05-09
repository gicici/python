#same as lists but they are immutable meaning they can't be changed
t= (1,2,3, 'one')
#another difference is that they uses parenthesis
print(t)
t= (1,2,3, 'one')
t.index(2)
#indexing means the position in the ordered list
print(t)
t= (1,2,3, 'one')
#they do not accept reassigning of variables.
#t[4] = (4,5,8)
print(t + t)