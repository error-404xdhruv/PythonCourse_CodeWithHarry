""" 
# python detect the dataype of the variable automatically
a = 2
b = 230.45621256

# we can declare a varible a string using any type of inverted commas.
# triple inverted can also declare multi line string
c = "hello world"
d = 'hello world'
e = '''hello
world'''
f = ''' "hello world" '''

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# we can check the datatype of a variable using the type function
print(type(a))
print(type(d))
print(type(e))

# variable names are case sensitive
a = 2.4
A = 32.56
print(a)
print(A)

# re-declare the variable
a = 2.90
print(a, A)  # printing more than one variable

print("The value of a:", a)

# assigning a single value to multiple variables
a = b = c = 17
print("the new value of a, b and c are:", a, b, c)

# assigning values to different variables in a single line
a, b, c = 1, "hello world", 8.9
print(a, b, c)

x = 69
print(type(x)) # output would be <class 'int'>

x = "69"
print(type(x)) # output would be <class 'str'>
 """
 
# how does '+' operator work with diff variables
a, b = 2, 5
print(a+b)

a, b= 'dhruv ', 'yadav'
print(a+b)