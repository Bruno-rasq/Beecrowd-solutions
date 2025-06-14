while True:
    N_JOGADORES, tam_tabuleiro = map(int, input().split())
    if N_JOGADORES == 0 and tam_tabuleiro == 0:
        break  # Fim da entrada

    POSICOES_ARMADILHAS = set(map(int, input().split()))
    N_JOGADAS = int(input())

    # Estrutura: jogador_id: [posição, penalizado]
    jogadores = {i: [0, False] for i in range(1, N_JOGADORES + 1)}
    vencedor = None

    jogadas_lidas = 0  # índice das jogadas efetivamente lidas
    turno = 0  # índice do turno para alternar jogadores

    while jogadas_lidas < N_JOGADAS:
        jogador_atual = (turno % N_JOGADORES) + 1
        posicao, penalizado = jogadores[jogador_atual]

        if penalizado:
            # Jogador perde a vez e não consome jogada
            jogadores[jogador_atual][1] = False  # remove penalização
            turno += 1
            continue

        # Só lê os dados se o jogador não está penalizado
        dados = list(map(int, input().split()))
        jogadas_lidas += 1

        nova_posicao = posicao + sum(dados)

        if nova_posicao in POSICOES_ARMADILHAS:
            jogadores[jogador_atual] = [nova_posicao, True]
        else:
            jogadores[jogador_atual] = [nova_posicao, False]

        if vencedor is None and nova_posicao > tam_tabuleiro:
            vencedor = jogador_atual

        turno += 1  # próximo jogador

    print(vencedor if vencedor is not None else 0)