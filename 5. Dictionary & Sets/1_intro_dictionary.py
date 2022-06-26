
""" 
Dictionary in Python is an unordered collection of data values, used to store data values like a map, which, unlike other data types that hold only a single value as an element, Dictionary holds key:value pair. Key-Value is provided in the dictionary to make it more optimised.  """
""" Note - Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly.  """


dict1 = {
    1 : "Geeks" , 
    2 : "For" , 
    3 : "Geeks"
}

# printing a dictionary
print(dict1)

# typecasting
print(list(dict1))

# dictionary with different data-types
dic1 = {
    'list1' : [1, 2, 3, "hello" , "world"],
    1 : "hello" ,
    "world" : "hello"
}

# accessing a particular key value
print(dic1['list1'])

# printint the value of a key using get function
print(dic1.get('world'))

# we can use both simple print and get function to print a particular value using its key, but there is one major difference b/w the two
""" get function return "None" when a key is not present in a dict. but simple print function would throw error in the same case """

print(dic1.get('bc'))
print(dic1['bc'])