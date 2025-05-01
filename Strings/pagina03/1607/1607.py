casos_teste = int(input())

for _ in range(casos_teste):
    a, b = input().split()
    
    total_trocas = 0
    
    for i in range(len(a)):
        total_trocas += (ord(b[i]) - ord(a[i])) % 26
        
    print(total_trocas)