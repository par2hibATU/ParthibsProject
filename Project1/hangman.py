import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)     #randomly chooses something from the list
    while "-" in word or ' ' in word:       #This will loop will be continued itself as long as it gets Dash or space in the word.
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)        #Set is an unordered collection of well defined objects. In sets words won't be repeated.
#This ^ set has been used to track which word has already guessed
    alphabet = set(string.ascii_uppercase)  #this set will list all the 26 English characters
    used_letters = set()    #what the user has guessed so far
    lives = 7
    while len(word_letters) > 0 and lives > 0:    #As I want to check all the words in the 'word_letter', I want to iterate through the whole list as long as the number of unchecked word is 0
        #letter used-(''.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have", lives, 'lives left and You have used these letters: ', ' '.join(used_letters))

        #what current word is (ie: W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input("Guess a letter: ").upper() #getting user input
        if user_letter in alphabet - used_letters:      #This condition checks if 'user_letter' is in the set difference between 'alphabet' and 'used_letters'.
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1 ##takes away a life if wrong guess made
                print('\nYour letter,',user_letter, 'is not in the word.')
        elif user_letter in used_letters:
            print("You have already used that character. Please try again!!")

        else:
            print("Invalid character")

    #gets here when len(word_letters) == 0 OR when lives == 0)
    if lives == 0:
        print("You died, sorry. The word was: ", word)
    else:
        print("You guessed the word", word, '!!')

hangman()


