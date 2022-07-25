# https://www.geeksforgeeks.org/reduce-in-python/?ref=lbp
# a very important article to understand the reduce() function

'''
Working :  

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.

# python code to demonstrate working of reduce()
'''

import functools

list = [1, 3, 4, 5, 1, 2]
print("The sum of all the elements of list is: ", end=" ")
print(functools.reduce(lambda a, b: a+b, list))

print("The largest element in the list is: ", end=" ")
print(functools.reduce(lambda a, b: a if a > b else b, list))