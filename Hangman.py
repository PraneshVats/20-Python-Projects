import random
from words import words

def get_valid_word(word):
    word=random.choice(words)
    while '-' in words or ' ' in word:
        word=random.choice(words)
        
    return word

def hangman():
    word=get_valid_word(word)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    