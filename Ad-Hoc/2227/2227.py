T = 1
while True:
    
    A, V = [int(x) for x in input().split()]
    if A == V == 0: break 

    aeroportos = [0] * A
    
    for _ in range(V):
        a, b = [int(x) for x in input().split()]
        aeroportos[a - 1] += 1
        aeroportos[b - 1] += 1
        
    _max = max(aeroportos)
        
    print(f"Teste {T}")
    for i in range(A):
        if aeroportos[i] == _max:
            print(i + 1, end=' ')
    print()
    print()
    T += 1
    
