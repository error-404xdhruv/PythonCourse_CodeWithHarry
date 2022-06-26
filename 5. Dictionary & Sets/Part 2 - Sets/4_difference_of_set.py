
# jisme se ghatana hain usme se hatana hain (common elements)

set1 = set()
for i in range (0, 5):
    set1.add(int(i))

set2 = set()
for i in range (4, 9):
    set2.add(int(i))

set3 = set1.difference(set2)
print(set3)