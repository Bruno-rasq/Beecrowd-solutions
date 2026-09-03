while True:
    n = int(input())
    if n == -1: break 

    accu = 0
    count = 0
    values = [int(x) for x in input().split()]
    for value in values:
        accu += value
        if accu % 100 == 0:
            count += 1
        
    print(count)