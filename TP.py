secretm="Hello World 3"
spam=list(secretm)
blanks='_'*len(secretm)
for i in range(len(secretm)):
    if spam[i]==' ':
        blanks = blanks[:i] + ' ' + blanks[i+1:]
for letter in blanks: # Show the secret word with spaces in between each letter.
        print(letter, end=' ')

