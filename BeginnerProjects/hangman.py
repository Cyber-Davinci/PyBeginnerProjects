import random

hangManPic = ['''
 +---+
     |
     |
     |
    ===
''',
'''
 +---+
 0   |
     |
     |
    ===
''',
'''
 +---+
 0   |
 |   |
     |
    ===
''',
'''
 +---+
 0   |
/|   |
     |
    ===
''',
'''
 +---+
 0   |
/|\  |
     |
    ===
''',
'''
 +---+
 0   |
/|\  |
/    |
    ===
''',
'''
 +---+
 0   |
/|\  |
/ \  |
    ===
'''
]

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def getRandomWord(wordlst):
    wordIndex = random.randint(0, len(wordlst)-1)
    return wordlst[wordIndex]

def displayBoard(missedLetters, correctLetters, secreteWord):
    print(hangManPic[len(missedLetters)])
    print()

    print("Missed Letters :", end=" ")
    for letter in missedLetters:
        print(letter, end=" ")
    print()

    blanks = '_' * len(secreteWord)
    for i in range(len(secreteWord)):
        if secreteWord[i] in correctLetters:
            blanks = blanks[:i] + secreteWord[i] + blanks[i+1:]
    
    for letters in blanks:
        print(letters, end=" ")
    print()

def getGuess(alreadyGuessed):
    while True:
        print("Guess a letter. ")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter!")
        elif guess in alreadyGuessed:
            print('You have already guessed that letter, please enter a different one')
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please Enter a letter")
        else:
            return guess


def playAgain():
    print("Do you want to play again (yes or no)")
    if input().lower().startswith("y"):
        return True
    else:
        print("Thanks for playing :-)")
        return False

print(" H A N G M A N")
missedLetters = ''
correctLetters = ''
secreteWord = getRandomWord(words)
gameDone = False ##pause for today, read biology

while True:
    displayBoard(missedLetters, correctLetters, secreteWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secreteWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secreteWord)):
            if secreteWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print(f"Yes! The secrete word is {secreteWord}! You have won")
            gameDone = True
            

    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(hangManPic) - 1:
            displayBoard(missedLetters, correctLetters, secreteWord)
            print(f"You have run out of guesses! after {str(len(missedLetters))} missed guesses and {str(len(correctLetters))} correct guesses, the word was {secreteWord}")
            gameDone = True

    if gameDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameDone = False
            secreteWord = getRandomWord(words)
        else:
            break
