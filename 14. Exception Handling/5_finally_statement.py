
try:
    a = int(input())
    print(1/a)
except Exception as e:
    print(e)
    exit()
# exit is necessary for the real affect of finally statement
finally:
    print("Done")

# finally would be printed irrespective of the outcome of the program

# when some exception occurs then Thank You would not be printed since we have used exit statement.
print("Thank You.")