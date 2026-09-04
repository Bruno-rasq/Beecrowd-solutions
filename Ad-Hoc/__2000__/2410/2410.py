notas_inseridas = int(input())
notas = set()  # Usamos um conjunto para armazenar valores únicos

for _ in range(notas_inseridas):
    nota = int(input())
    notas.add(nota)  # `add` no set é mais eficiente que verificar e adicionar na lista

print(len(notas))