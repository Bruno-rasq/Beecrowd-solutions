while True:
    
    n_selecoes, m_partidas = [int(x) for x in input().split()]
    
    if n_selecoes == m_partidas == 0: break

    pontuacao_total = 0
    for _ in range(n_selecoes):
        selecao, ponto = input().split()
        pontuacao_total += int(ponto)
        
    n_empates = (3 * m_partidas) - pontuacao_total
    print(n_empates)