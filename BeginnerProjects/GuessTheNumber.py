# This is a Guess The number Game

import random

guessesTaken = 0

PlayerName = input("Hello! What is your name?")

number = random.randint(1,20)
print(f"Well Hello {PlayerName} i am thinking of a number between 1 to 21.")
for guessesTaken in range(4):
    guess = input("Take a guess. ")
    guess = int(guess)
    
    if guess < number:
        print("Your Guess is too Low")
    if guess > number:
        print("Your Guess is too High")
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken+1)
    print(f"Congrats {PlayerName}! You've guessed my number in {guessesTaken} guesses")

if guess != number:
    number = str(number)
    print(f"Nope the number i was guessing is {number}")