n = int(input())
palavra = input()

def comparar(correta, errada):
    count = sum(i for i in range(len(correta)) if correta[i] == errada[i])
    return count

melhor_correspondencia = None
max_correspondencias = 0

for _ in range(n):
    curr = input()
    if len(palavra) != len(curr):
        break
    
    correspondencias = comparar(curr, palavra)

    if correspondencias > max_correspondencias:
        max_correspondencias = correspondencias
        melhor_correspondencia = curr

if melhor_correspondencia and max_correspondencias >= (len(palavra) / 2):
    print(melhor_correspondencia)
else:
    print("repetir")