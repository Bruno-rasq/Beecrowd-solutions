numero_jogadores, numero_partidas = [int(x) for x in input().split()]

n_jogadores_gols_td_partidas = 0

for i in range(numero_jogadores):
    placar = [int(x) for x in input().split()]
    contador = 0
    for j in range(numero_partidas):
        if placar[j] == 0:
            break
        contador += 1
    if contador == len(placar):
        n_jogadores_gols_td_partidas += 1
        
print(n_jogadores_gols_td_partidas)