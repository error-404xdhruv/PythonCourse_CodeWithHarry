import random

computer = random.randint(1, 100)
user = int(-1)
count = 1
while(user != computer):
    user = int(input("Guess the Number! "))
    if (user == computer):
        print(
            f"Yes you guessed it correctly. You took {count} turns to reach here.")
        break
    elif (user < computer):
        print("Try Again. You guessed a smaller number.")
    elif (user > computer):
        print("Try Again. You guessed a higher number.")
    count += 1

with open("project2_highscore.txt", "r") as file:
    currentHighScore = int(file.read())
    if (count < currentHighScore):
        print("New HighScore!")
        with open("project2_highscore.txt", "w") as file:
            file.write(str(count))
