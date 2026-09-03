l = int(input())
c = int(input())

def isEven (num):
    return num % 2 == 0

if (isEven(c) and isEven(l)) or (not isEven(c) and not isEven(l)):
    print(1)
else:
    print(0) 