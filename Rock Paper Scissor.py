from gc import is_finalized
import random

def play():
    user = input("What's your choice? 'R' for rock, 'P' for Paper, 'S' for Scissors\n")
    computer= random.choice(['R','P','S'])
    
    
    if user == computer:
        return 'It\'s a tie'
    
    if is_finalized(user, computer):
        return 'You Won!'
    
    return 'You Lost'
    
    def is_win(player, opponent):
        if( player=='R' and opponent=='S') or (player=='S' and opponent=='P') \
            or (player == 'P' and opponent=='R'):
            return True
            