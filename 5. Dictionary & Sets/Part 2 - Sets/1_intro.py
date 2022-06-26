
""" A Set is an unordered collection (i.e., values are not stored in the sequence way we add them to, values are always stored in a sorted way) data type that is iterable, mutable and has no duplicate elements. Python’s set class represents the mathematical notion of a set. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. This is based on a data structure known as a hash table. Since sets are unordered, we cannot access items using indexes like we do in lists. """

""" Set is a collection of non-repetitive elements. """
""" A set is always sorted (acc to ASCII table) """

# create a set
from http.client import PRECONDITION_REQUIRED
from multiprocessing import Semaphore


s = {2, 3, 4, 1, 5, 1}
print(s)

# creating a empty set
sEmpty = set()
print(sEmpty)
print(type(sEmpty))

# adding elements to a set
s.add(4)
s.add(10)
s.add(9)
s.add(9)
# if you would add same element multiple times, then even it would be added only once
print(s)

# we can only add one element at a time as add function does not support multiple arguments
s.add('a')
print(s)

# we can not add lists and dictionary in a set as set is unhashable and lists and dictionary are hashable (i.e., they can be modified)
# but we can add tuples to a set
s.add((1, 4, 3))
print(s)

# len() function : returns the length of the set
print(len(s))

# remove() function: removes the specific item , if not present then throws error
s.remove(1)
print(s)

# pop() function : removes an element (randomly) from the set
s.pop()
print(s)

# clear function : clears the set
s.clear()
print(s)