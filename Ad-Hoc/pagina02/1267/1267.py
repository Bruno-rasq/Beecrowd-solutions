while True:
    num_ex_alunos, num_eventos = [int(x) for x in input().split()]
    if num_ex_alunos == num_eventos == 0:
        break
    
    contagem_participacoes = [0 for i in range(num_ex_alunos)]
    for i in range(num_eventos):
        participacoes = [int(x) for x in input().split()]
        for idx, participacao in enumerate(participacoes):
            contagem_participacoes[idx] += participacao
            
    print("yes" if num_eventos in contagem_participacoes else "no")