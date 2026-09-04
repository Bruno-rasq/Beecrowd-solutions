while True:
    init, target = input().split()
    
    if init == target == "*": break
    
    movs = 0
    for i in range(len(target)):
        if init[i] != target[i]:
            if i == 0 or init[i-1] == target[i-1]:
                movs += 1
                
    print(movs)