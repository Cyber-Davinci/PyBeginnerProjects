## Lets have an array or list of words and selct a random word
## Give the user a hint of what the word might be
##Let's see how this goes
import random


words = ['Hello','World','Time','Space','Week', 'Weak', 'Code','Python','Programmmer', 'Hacker']
guessedWord = random.choice(words)
chances = 0



def giveHint(guessedWord):
    first_letter = guessedWord[0:1]
    reverseWord = guessedWord[::-1]
    last_letter = reverseWord[0:1]
    print(f"first letter is {first_letter.upper()} and last letter is {last_letter.upper()} ")

print('Hello there whats your name! ')

user_name = input()
print(f'well hello {user_name} i am thinking of a word from list of words above')
for chances in range(3):
    guess = input('Take a guess: ')
    guess = guess.lower()
    if chances ==  1:
        print('Hint!')
        giveHint(guessedWord)
    if guessedWord.lower() == guess:
        break
if guessedWord.lower() == guess:
    print(f"Congrats {user_name} your'e a genius ")
    print(f"The word i guessed is exactly '{guessedWord.upper()}'")
if guessedWord.lower() != guess:
    print(f"oops you lost...the word i guessed is {guessedWord}")


    

