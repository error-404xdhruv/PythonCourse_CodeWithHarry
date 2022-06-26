
dict = {1 : 'hello' , 2 : 'world' , 'name' : {1 : 'dhruv' , 2 : 'yadav'}}
print(dict[1])
print(dict['name'])

# here dict would be a nested dictionary as name is a dictionary itself

# accessing elements in a nested dictionary
dict2 = {
    1 : {1 : 'hello' , 2 : 'world'} ,
    2 : {('hello', 1) , ('world' , 2)}
}
print()
print(dict2[1])

# accessing an element from a nested dictionary
print()
print(dict2[1][2])
