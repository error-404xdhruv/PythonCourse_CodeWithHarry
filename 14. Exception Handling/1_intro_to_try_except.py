# Lets Create a game which goes like this :
""" 
Program asks the user to enter some number
if the number is greater than 10 program would print some line
program will go till user enter q (which is meant to quite the program)

Now this may happen that user is DUMB and s/he enter a char or string instead of some number, then in the normal cases the program woudl crash but we woudl learn how to avoid this and this is k/a Exception Handling
"""
from sys import excepthook


while (True):
    print("Press 'Q' to Quit or ", end="")
    a = input("Enter a number: ")
    if (a == 'Q'):
        break
    # now the program wont crash
    try:
        if (int(a) > 10):
            print("Number is Greater than 10.")
        elif(int(a) <= 10):
            print("Number is smaller than or equal to 10.")
    except Exception as error:
        print(f"Your input resulted in error: {error}")

print("Thank You")
