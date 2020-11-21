def display(missedLetters,correctLetters,secretm):
    
    blanks = '_' * len(secretm)
    for i in range(len(secretm)):
        if spam[i]==' ':
            blanks = blanks[:i] + ' ' + blanks[i+1:] 
    for i in range(len(secretm)): # Replace blanks with correctly guessed letters.
        if secretm[i] in correctLetters:
            blanks = blanks[:i] + secretm[i] + blanks[i+1:]
    for letter in blanks: # Show the secret word with spaces in between each letter.
        print(letter, end=' ')
        print()
