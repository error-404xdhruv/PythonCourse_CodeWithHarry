# to make this game we would be using random module
# Game would go like this: Player chooses a turn and at the same time Computer chooses a turn and then the Winner would be decied on the basis of the rules of the game

from cgi import print_form
import random

def game(player, computer):
    if (player == computer):
        print("Draw")
    elif ((computer == 'R' and player == 'S') or (computer == 'S' and player == 'P') or (computer == 'P' and player == 'R')):
        print("Computer Wins!")
    else:
        print("Player Wins!")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = input(
    "Please type 'R' for Rock, 'S' for Scissor and 'P' for Paper: ")
print("Player Chooses: ")
if (player == 'R'):
    print(rock)
elif (player == 'S'):
    print(scissors)
elif (player == 'P'):
    print(paper)

turn = ['R', 'S', 'P']
computer = random.choice(turn)
print("Computer Chooses: ")
if (computer == 'R'):
    print(rock)
elif (computer == 'S'):
    print(scissors)
elif (computer == 'P'):
    print(paper)

game(player, computer)