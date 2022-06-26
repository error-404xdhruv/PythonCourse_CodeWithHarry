
# creating a dictionary using basic method
mydict0 = {
    1 : "one" ,
    2 : "two",
    '3' : "three",
    "hello" : "world"
}
print(mydict0)

# creating a dictionary using dict() function
mydict = dict({'1': "Geeks", 2: "for", 3: "Geeks"})
print(mydict)

# using dict() function but in pairs
mydict2 = dict([(1, 'hello'), (2, 'world')])
print(mydict2)

""" Complexities for Creating a Dictionary:

Time complexity: O(len(dict))
Space complexity: O(n) """