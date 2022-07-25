
# https://www.geeksforgeeks.org/python-string-join-method/?ref=gcse

'''
join() is an inbuilt string function in Python used to join the elements of the sequence/list/tuples/or any iterable sequence seperated by a string separator. This function joins the elements of a sequence and makes it a string.
'''

# method 1
list1 = ["hello", "world", "i", "am", "back"]
s = "-"
s = s.join(list1)
print(s)

# method 2
list2 = ["how", "to", "win", "friends"]
print(" ".join(list2))