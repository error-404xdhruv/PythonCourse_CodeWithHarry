""" 
Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java). In a simple language, a list is a collection of things, enclosed in [ ] and separated by commas. Lists are the simplest containers that are an integral part of the Python language. Lists need not be homogeneous always which makes it the most powerful tool in Python. A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are mutable, and hence, they can be altered even after their creation.
the indexing of a list is done with 0 being the first index. Each element in the list has its definite place in the list, which allows duplicating of elements in the list

Lists need not be homogeneous always which makes it the most powerful tool in Python. A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are mutable, and hence, they can be altered even after their creation.
"""

a = [1, 2, 3, 4, 564343, 2321]

# printing lists using print function
print(a)

a[0] = 100
print(a)

# empty list
b = [] 
print(b)

# since a list can contain item of different datatype
t = 1
u = "dhruv"
z = [t, u]
print(z)

# list slicing
circle = ["dhruv", "abh1shank" , "abhishek", "shri" , "av1ral"]
# it means print the elements of list from index 0 to 3
print(circle[0:4])
# print from begin to end
print(circle[:])
# print from i to end
print(circle[1:])
# print from begin to some index i-1
print(circle[:5])
# since python also support -ve indexing
print(circle[-3:-1])