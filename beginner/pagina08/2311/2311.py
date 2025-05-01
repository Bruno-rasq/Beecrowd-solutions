competidores = int(input())

for _ in range(competidores):
    nome = input()
    dificuldade = float(input())
    notas = [float(x) for x in input().split()]
    
    maior = max(notas)
    menor = min(notas)
    
    notas.remove(maior)
    notas.remove(menor)
    
    soma = sum(notas)
    nota = soma * dificuldade
    
    print(f"{nome} {nota:.2f}")