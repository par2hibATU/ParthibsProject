import random


def play():
    user = input("Pick your choice: \n'r' for rock, 'p' for paper, 's' for scissors")
    comp = random.choice(['r', 'p', 's'])

    if user == comp:
        return "it's a tie"

    if is_win(user, comp):
        return "You won"

    return "you lost"


def is_win(player, oponent):
    if (player == 'r' and oponent == 's') or (player == 's' and oponent == 'p') or (
            player == 'p' and oponent == 'r'):
        return True
    return False


print(play())
