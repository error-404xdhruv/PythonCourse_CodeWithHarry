'''
A list contains the multiplication table of 7. Write a program to convert it to a vertical string of same numbers
'''
# making a list using comprehension
list1 = [str(i*7) for i in range (1, 11)]
print(list1)

# using join function
print('\n'.join(list1))