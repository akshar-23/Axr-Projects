def collatz(num):
    while num > 1:
        if num % 2 == 0:
            print(num//2)
            num = num //2
        elif num % 2 ==1:
            print(3*num+1)
            num = 3*num+1
        else:
            print(num)

def getNum():
    global num
    num = (input("> "))
    try:
        num = int(num)
    except ValueError:
        print('plese enter a number')
        getNum()
getNum()
collatz(num)
