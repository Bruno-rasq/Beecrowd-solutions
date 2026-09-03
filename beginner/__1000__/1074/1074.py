i = int(input())

for _ in range(i):
    curr = int(input())

    if curr == 0:
        print('NULL')

    elif curr % 2 == 0:
        if curr > 0:
            print('EVEN POSITIVE')
        else:
            print('EVEN NEGATIVE')
    else:
        if curr > 0:
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')