# write a program to print the greatest of 4 numbers entered by user
print("Enter 4 Numbers: ")
list = []
max = int(0)
for i in range(0, 4):
    a = int(input())
    list.append(a)
    if (list[i] > max):
        max = list[i]

print("Greatest:",max)