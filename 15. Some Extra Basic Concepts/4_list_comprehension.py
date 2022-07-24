# List Comprehension is an elegant way to create a list based on existing list, remember the phrase based on an exisiting list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Suppose we have to create a list b which stores all the even numbers from list a

# method 1
ok1 = []
for i in a:
    if ((i & 1) != 1):
        ok1.append(i)
print(ok1)

# method 2 (list comprehension)
ok2 = [i for i in a if((i & 1) != 1)]
print(ok2)

# we can do the same for Set Comprehension and Dictionary Comprehension