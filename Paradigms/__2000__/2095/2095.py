N = int(input())
quadradonia = [int(x) for x in input().split()]
nlogonia = [int(x) for x in input().split()]

quadradonia.sort()
nlogonia.sort()

ANS = 0
ptr1 = 0
ptr2 = 0
N_soldier = nlogonia[ptr1]
Q_soldier = quadradonia[ptr2]

while True:
    try:
        
        if N_soldier > Q_soldier:
            ANS = ANS + 1
            ptr1 = ptr1 + 1
            ptr2 = ptr2 + 1
            N_soldier = nlogonia[ptr1]
            Q_soldier = quadradonia[ptr2]
            
        else:
            ptr1 = ptr1 + 1
            N_soldier = nlogonia[ptr1]

    except: break 

print(ANS)