while True:
    temporadas, duracao_episodio = [int(x) for x in input().split()]

    if temporadas == duracao_episodio == -1: break 
        
    ep_por_temporadas = [int(x) for x in input().split()]

    total_episodios = 0
    for i in range(temporadas):
        total_episodios += ep_por_temporadas[i] * (temporadas - i)

    print(total_episodios * duracao_episodio)