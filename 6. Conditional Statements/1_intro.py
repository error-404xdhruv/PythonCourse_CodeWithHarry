
# if-else and elif statements
age = int(input("Enter your age: "))
if (age >= 18):
    print("You are eligible to vote !")
elif (age >= 11 and age < 18):
    print(f"YOu are eligible to vote, but after {18-age} years only !")
else :
    print("Goto hell !")

# multiple if statements
temp = int(56)
if (temp == 56):
    print("Yes")

if (temp >= 56):
    print("Yes")
else:
    print("No")