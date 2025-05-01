notas = [float(x) for x in input().split()]

maior = max(notas)
menor = min(notas)
notas.remove(maior)
notas.remove(menor)

nota_final = sum(notas)
print(f"{nota_final:.1f}")