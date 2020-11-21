spam=list('HOLLYWOOD')
p=input()

for p in range(len(spam)):
    spam[:p]='x'
        
print(spam)






