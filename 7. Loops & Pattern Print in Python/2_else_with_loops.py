for i in range (1, 11):
    print(i)
else:
    print("Loops iterated Succesfully.")
print("Success")

# the question is why are we using else statement, if we can use a simple print statement or we can start writing the code after the loop as it is ? So, the answer is that code inside else statement will be executed only when the loop is iterated completely, i.e., it would not execute the code inside else statement if we have used break statement inside the loop or somehow due to any reason we stopped the execution of loop in between

for i in range (1, 11):
    print(i)
    if (i==5):
        break
else:
    print("Success !")
print("Not Success")