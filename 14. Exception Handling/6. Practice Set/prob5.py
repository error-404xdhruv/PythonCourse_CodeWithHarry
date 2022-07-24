'''
Store the multiplication table generated in Problem 3 in a file names table.txt
'''
num = int(input("Enter your number: "))
table = [num*i for i in range(1, 11)]
print(table)
with open ('table.txt', 'w') as file:
    file.write(str(table))