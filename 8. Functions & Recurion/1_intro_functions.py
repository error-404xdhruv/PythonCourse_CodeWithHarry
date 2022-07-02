def summ(a, b):
    return a+b

a = int(input())
b = int(input())
print(summ(a, b))

# concept of default parameter value or default argument value

# here Stranger would work as default argument value
def greetWithDefaultArgument(name = "Stranger"):
    print("Hello,", name)

def greet(name):
    print("Hello", name)

name = input()
greet(name)
greetWithDefaultArgument()
greetWithDefaultArgument("dhruv")

# the below line woudl throw error
greet()