
list = [2, 1, 4, 5, 12, 12, 43, 5]

# knowing the size of list
print(len(list))

# sort list
list.sort()
print(list)

listChar = ['d', 'e', 'a']
listChar.sort()
print(listChar)

""" # this list would not be able to sort
listNew = [1, 2, "hello" , 43, 3, 4, 1, 'f'] 
listNew.sort()
print(listNew) """

# reverse a list
list.reverse()
print(list)

# append function : adds an item at the last of the list --> similar to push_back in vectors in C++
list.append(100)
print(list)

# insert function : adds an item at some specific index
list.insert(2, 200)
print(list)

# pop function : removes the element from some specific index
list.pop(2)
print(list)

# if we dont specify any index then pop function removes the last element of the list
list.pop()
print(list)

# remove function : removes a particular element from the list if it is present and only once elements is removed if its present more than once in the list
list.remove(5)
print(list)

""" list.remove(200)
print(list) """  # it would give error as 200 is not present in the list

# index function : returns the index of the first occurence of an element
print(list.index(12))