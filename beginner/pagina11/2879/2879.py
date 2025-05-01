partidas = int(input())

vitorias = 0
for _ in range(partidas):
    n = int(input())
    if n == 2 or n ==  3:
        vitorias += 1
        
print(vitorias)