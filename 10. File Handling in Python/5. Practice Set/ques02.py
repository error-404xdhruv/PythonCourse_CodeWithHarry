
score = int(input("Enter your Score: "))

with open('highscore.txt', 'r') as file:
    hiscore = file.read()
    temp = int(hiscore)

if (temp >= score):
    print("Retry ; HighScore: ", end=" ")
    print(temp)
else:
    print("New Highscore.")
    with open('highscore.txt', 'w') as file:
        file.write(str(score))