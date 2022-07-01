# write a program to find whether a given number is prime or not using loops
n = int(input())
flag = True
for i in range (2, n):
    if (n%i==0):
        flag = False
        break

if (flag):
    print("Yes, Prime Number.")
else:
    print("Composite Number.")