import random

def play():
    user = input("Hihi, What's your choice??? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    # r > s , s > p, p > r
    if win(user, computer):
        return 'You won!!!!'
    
    if win(computer, user):
        return 'You LOST!!!'
    


def win(player,opponent):
    if (player == 'r' and opponent == 's' ) or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
        return True
    
print(play())