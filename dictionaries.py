#dictionaries are mapping i.e a collection of objects that are sorted by a key
#instead of indexing they use keys
my_dict = {'key1': 'value', 'key2': 'value2'}
my_dict['key1']= 'value'
print(my_dict['key1'])
d = {}
print(d)
#this is assigning a value in dictionaries
d['animal'] = 'Lion'
d['answer'] = '42'
print(d['animal'][::-1])
#nesting means a dictionary inside a dictionary
#d = {'k1': {'nestkey': {}}}
d = {'k1':{'nestkey':{'subkey':'value'}}}
f = {}
f ['key1'] = 1
f ['key2'] = 5
f ['key3'] = 3
#this returns keys but if you want it to return values use the .values() method and .items displays all the items such as the keys and values
print(f.keys())