a = int(input("Enter a: "))
b = int(input("Enter b: "))
try:
    print(round(a/b, 2))
except ZeroDivisionError as e:
    print("Infinite")