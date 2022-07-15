
# we have to put that code in try which can produce error
try:
    a = int(input("Enter a integral Value: "))
    print(round(1/a, 2))
except ValueError as e:
    print("Please enter a valid Integer and try again!")
except ZeroDivisionError as e:
    print("0 is not a permissible Value.")
except Exception as e:
    print("An error occured.")