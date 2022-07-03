# Take an integer as input from user and if it is greater than the prev stored value in the file then update the file with the new integer

n = int(input("Enter your Score: "))
data = int(0)
with open('hiscore.txt', 'r') as file:
    data = int(file.read())

if (n > data):
    with open('hiscore.txt', 'w') as file:
        file.write(n)

with open('hiscore.txt', r) as file:
    print(file.read())