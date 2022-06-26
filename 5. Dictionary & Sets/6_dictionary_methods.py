dict = {1: 'C', 2: 'C++', 3: 'Python'}

# copy function : returns an exact copy of the dictionary
dict2 = dict.copy()
print(dict2)

# clear funtion: removes all the elements from a dictionary
dict.clear()
print(dict)

# get function: return the value at a specific key
print(dict2.get(3))

# items() – Returns a list containing a tuple for each key value pair
print(dict2.items())

# popitems() - deletes the last element of the dictionary
dict2.popitem()
print(dict2)

# pop() - deletes the element with a specific key
dict2.pop(2)
print(dict2)

# keys() – Returns a list containing dictionary’s keys
print(dict2.keys())

# update() – Updates dictionary with specified key-value pairs
dict2.update({2: 'C++' , 3: 'Python'})
print(dict2)

# values() – Returns a list of all the values of dictionary
print(dict2.values())