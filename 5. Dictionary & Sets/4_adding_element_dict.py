
# creating an empty dictionary
dict = {}
print("\nEmpty Dictionary: ")
print(dict)

# adding elements to dictionary
dict['hello'] = 'world'
dict[1] = 'bhaag jaao'
print(f"\nPrint Dictionary after Adding Elements: \n{dict}")

# adding set of values to single key
dict['Value_Set'] = "hello" , 1, 22
print(f"\nPrint Dictionary after Adding set of elements: \n{dict}")

# updating value of an existing key
dict[1] = 'nikal jaao'
print(f"\nPrint Dictionary after updating value of key '1': \n{dict}")

# adding nested key value to a dictionary
dict[10] = {'Nested Value' : {1, 2, 3} , 'Nested 2': {3, 2, 1}}
print(f"\nPrint Dictionary after adding nested key value: \n{dict}")

