import random

def play():
    user = input("Enter your Choice \n1.Rock(r)\n2.Paper(p)\n3.Scissors(s)\n")
    computer = random.choice(['r', 'p', 's'])

    if user==computer:
        return "It was a tie"

    if is_win(user,computer):
        return "You Win!!!"
    return "You Loose.."

def is_win(player,computer):
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's'and computer == 'p'):
        return True

while(True):
    lets_play = input("Do you want to play the game (yes/no):- ")
    if lets_play == "yes":
        print(play())
    else:
        break
