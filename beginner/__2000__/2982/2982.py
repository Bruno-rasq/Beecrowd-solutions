dados = int(input())

bolsas = 0
despesas = 0

for _ in range(dados):
    a, valor = input().split()
    
    if a == "V": 
        bolsas += int(valor)
    else:
        despesas += int(valor)
        
print(
    "NAO VAI TER CORTE, VAI TER LUTA!" 
    if bolsas < despesas else "A greve vai parar."
)