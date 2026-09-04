while True:
    N, M = [int(x) for x in input().split()]
    
    if N == M == 0: break
    
    tickets_originais = {x: 0 for x in range(1, N + 1)}
    
    tickets_evento = [int(x) for x in input().split()]
    
    for i in range(M):
        ticket = tickets_evento[i]
        tickets_originais[ticket] += 1
        
    falsos = 0
    for ticket in tickets_originais:
        if tickets_originais[ticket] > 1: falsos += 1
        
    print(falsos)
    
