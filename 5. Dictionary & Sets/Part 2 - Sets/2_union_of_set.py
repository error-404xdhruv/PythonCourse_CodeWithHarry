
# union of two sets
set1 = {"hello", "world", "good day"}
set2 = {"good bye", "nikal yha se"}

# method 1
new1 = set1.union(set2)
print(new1)

# method 2 - using '|' operator
new2 = set2 | set1
print(new2)
print(type(new1), type(new2))
