n = int(input())

for _ in range(n):
    poder = int(input())
    
    print("Inseto!" if poder <= 8000 else "Mais de 8000!")