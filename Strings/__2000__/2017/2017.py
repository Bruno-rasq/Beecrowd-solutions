
def hamming_distance(s1, s2):
    distancia = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distancia += 1
    return distancia
    

string_principal = input()
k = int(input())

indice = -1
menor_distancia = float('inf')

for i in range(5):
    palavra = input()
    distancia = hamming_distance(string_principal, palavra)
    
    if distancia < menor_distancia:
        menor_distancia = distancia
        indice = i + 1

print(indice)

print(menor_distancia if menor_distancia <= k else -1)