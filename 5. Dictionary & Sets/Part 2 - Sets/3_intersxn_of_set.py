
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4, 9, 0}

# method 1
new1 = set1.intersection(set2)
print(new1)

# method 2 - using '&' operator
new2 = set1 & set2
print(new2)