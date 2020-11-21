def welcome():
    print("LET'S PLAY DUMBSHERAS")
    print()
    print("(This is a two player game. The first player will enter the movie name and the other player will guess the name of the movie in limted number of tries)")
    print()

def b_or_h ():
    print("Is your movie from Hollywood or Bollywood?")
    spam = input()
    if spam.upper() == "HOLLYWOOD" or spam.lower().startswith('h')==True:
        spam="HOLLYWOOD"
        lives = list(spam)
    elif spam.upper() == "BOLLYWOOD" or spam.lower().startswith('b')==True:
        spam="BOLLYWOOD"
        lives = list(spam)

def moviename():
    print("Enter the name of the movie")
    secretm = input()
    return secretm

def displayBoard(missedLetters, correctLetters, secretm):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretm)

    for i in range(len(secretWord)): # Replace blanks with correctly guessed letters.
        if secretm[i] in correctLetters:
            blanks = blanks[:i] + secretm[i] + blanks[i+1:]

    for letter in blanks: # Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
     while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess
    
def playAgain():
    # This function returns True if the player wants to play again; otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')




missedLetters = ''
correctLetters = ''
gameIsDone = False

while True:
    welcome()

    b_or_h()
    
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses,the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break

