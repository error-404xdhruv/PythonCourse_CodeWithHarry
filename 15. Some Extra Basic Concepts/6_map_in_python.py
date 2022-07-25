'''
map function is used when we have to perform the same function on each element of a given iterable sequence (list, tuple, etc), it returns a list
'''

# example 1


def into2(n): return n*2


list1 = [1, 2, 3]
print(list(map(into2, list1)))

# example 2
print(list(map(lambda x: x*2, list1)))

# example 3
# map() can listify the list of strings
list2 = ['hello', 'world']
print(list(map(list, list2)))