
""" A tuple is a sequence of immutable Python objects. Tuples are just like lists with the exception that tuples cannot be changed once declared. Tuples are usually faster than lists. """

tuple = (1, 2, 3, 4, 5, 1, 1, 1, 2)

print(tuple)
print(tuple[1])

# tuple[1] = 2 # this woudl give an error as tuples are unchangable

# count function : returns the number of occurence a particular element occurs in a tuple
print(tuple.count(1))
print(tuple.count(100))

# index function : return the index of the first occurence of an element in a tuple
print(tuple.index(5))
print(tuple.index(1))