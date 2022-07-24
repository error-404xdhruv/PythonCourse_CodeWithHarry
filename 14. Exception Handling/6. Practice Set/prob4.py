'''
Write a program to display a/b where a and b are integers. If b=a, display infinte by handling the ZeroDivisionError.
'''

a = int(input("Enter a: "))
b = int(input("Enter b: "))
try:
    print(round(a/b, 2))
except ZeroDivisionError as e:
    print("Infinite")