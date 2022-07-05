# Take an integer as input from user and if it is greater than the prev stored value in the file then update the file with the new integer

score = input("Enter your Score: ")

with open('hiscore.txt', 'r') as file:
    hiscore = file.read()

if (score > hiscore):
    with open ('hiscore.txt', 'w') as file:
        file.write(score)
else :
    print("You did not score enough!")
