spam='hollywood'
p=0
wordlist=spam[:p]
replacelist='x'*(p+1)
for p in range(len(spam)):
    spam = spam.replace(wordlist,replacelist)
    p=p+1
    print(spam)
