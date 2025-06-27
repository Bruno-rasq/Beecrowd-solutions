# Para cada cidade é computado as distâncias para as demais o max
# da distância para cada uma das demais cidades, entre os maiores
# valores a resposta será o minimo destes.

# o algoritmo de Floyd-Warshall ajuda a calcular os caminhos indiretos.

#      0   1   2   3
#  0   0   2   4   3  -> max(2, 4, 5) = 4
#  1   2   0   6   1  -> max(2, 6, 1) = 6
#  2   4   6   0   5  -> max(4, 6, 5) = 6
#  3   3   1   5   0  -> max(3, 1, 5) = 5

#  min(4, 6, 6, 5) -> 4
  

n_cidades, n_rotas = [int(x) for x in input().split()]

rotas = { x: {} for x in range(n_cidades)}
for _ in range(n_rotas):
    origem, destino, custo = [int(x) for x in input().split()]
    rotas[origem][destino] = custo
    rotas[destino][origem] = custo
    

dist = [[float('inf')] * n_cidades for _ in range(n_cidades)]

for i in range(n_cidades):
    dist[i][i] = 0 #distancia para si mesmo sempre 0


for origem in rotas:
    for destino in rotas[origem]:
        custo = rotas[origem][destino]
        dist[origem][destino] = min(dist[origem][destino], custo)

# Floyd-Warshall: completar a matriz com os menores caminhos indiretos
for k in range(n_cidades):
    for i in range(n_cidades):
        for j in range(n_cidades):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                

max_dists = []
for distancia in dist: max_dists.append(max(distancia))
    
print(min(max_dists))