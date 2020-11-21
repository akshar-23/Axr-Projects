numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
remainder = []
for i in range (14):
    try:
        remainder.append(36%numb[i])
    except ZeroDivisionError:
        remainder.append("zero Error")
print (remainder)
