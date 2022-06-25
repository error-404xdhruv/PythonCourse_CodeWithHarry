
# global variables
word = "i love geeksforgeeks"

def f():
    print(word)

f()

# local variables
def printWord():
    a = 9
    print(a)

printWord()

# variable word can be used by any function in this whole program but variable a would not be, the scope of variable a is limited to printWord function only