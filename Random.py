import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f'Guess a number between 1 and {x}: '))
        print(guess)
        if guess<random_number:
            print('Sorry, guess again, Too Low.')
        elif guess>random_number:
            print('Sorry, guess again, Too High.')
            
    print(f'Yay, congrats. You have guessed the number {random_number} correctly')
            
    
def computer_guess(x):
    low=1
    high=x
    feedback = ''
    while feedback != 'c' and  :
        if low != high:
            guess = random.randint(low, high)
        else:
            guess=low #could also be high 
            feedback=input(f'Is {guess} too high (H), too low (L), orcorrect ')
            if feedback == 'h':
               high=guess-1
            elif feedback=='l':
               low  = guess+1
            
    print(f'Yay! The computer guesssed your number.{guess}, correctly')
    
    
guess(10)
