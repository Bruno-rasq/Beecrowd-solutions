x1, y1, x2, y2 = [int(x) for x in input().split()]

i = 1
while x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:

    n_meteoritos = int(input())
    
    meteoritos = 0
    for _ in range(n_meteoritos):
        x, y = [int(x) for x in input().split()]
        
        if x1 <= x <= x2 and y2 <= y <= y1:
            meteoritos += 1
            
    print(f"Teste {i}")
    print(meteoritos)
    
    i+= 1 
    x1, y1, x2, y2 = [int(x) for x in input().split()]