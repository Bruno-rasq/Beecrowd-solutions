n = int(input())
for _ in range(n):
    
    texto = input().split()
    palavra = input()
    indice = 0
    indices = []
    
    for palavra_atual in texto:
        if palavra_atual == palavra:
            indices.append(str(indice))
        indice += len(palavra_atual) + 1
    
    print(" ".join(indices) if len(indices) != 0 else -1)