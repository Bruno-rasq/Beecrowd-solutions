
#sliding window.

n = int(input())
lista = [int(x) for x in input().split()]

escadas_possiveis = 0

i = 0
while i < n - 1:
    degrau = lista[i + 1] - lista[i]
    comprimento = 1
    j = i + 1
    
    while j < n - 1 and lista[j + 1] - lista[j] == degrau:
        comprimento += 1
        j += 1
        
    if comprimento >= 1:
        escadas_possiveis += 1
        i = j  # pula para o final da escada
    else:
        i += 1  # não formou escada, avança só 1

print(escadas_possiveis if escadas_possiveis > 0 else 1)