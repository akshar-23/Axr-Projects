import sys
print('Choose the type of operation you want to do')
while True:
    print('Type m, d, a, s or q for (m)ultiply, (d)ivide, (a)dd, (s)ubtract, (q)uit respectively')
    while True:
        optype=input()
        if optype=='q':
            sys.exit()
        if optype=='m' or optype=='d' or optype=='a' or optype=='s':
            break
        print('Enter one of m,d,a,s or q')

    if optype=='m':
        print('Enter two number whose multiplication you want to find.')
        num1=input()
        num2=input()
        mul=float(num1)*float(num2)
        print(mul)
    elif optype=='d':
        print('Enter two number whose division you want to find.')
        num3=input()
        num4=input()
        div=float(num3)/float(num4)
        print(div)
    elif optype=='a':
        print('Enter two number whose addition you want to find.')
        num5=input()
        num6=input()
        add=float(num5)+float(num6)
        print(add)
    elif optype=='s':
        print('Enter two number whose subtraction you want to find.')
        num7=input()
        num8=input()
        sub=float(num7)-float(num8)
        print(sub)
    
