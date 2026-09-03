# CODIGO USANDO PROGRAMAÇÃO DINÂMICA.

MEM = {1: 2}     # Armazena os resultados pré computados.
last_K = 1       # Guarda o último valor chave a ser inserido na MEM
j = 1            # Variavel que auxiliar a calcular o resultado.

N = int(input())
for _ in range(N):
    K = int(input())

    if K > last_K:                # Quando K for maior que lastK atualiza MEM
        reg = MEM[last_K]         # Pega o ultimo valor computado
        while last_K <= K:        # Itera até que lastK tenha o tamanho de K
            reg += j + 1        
            j += 1
            last_K += 1
            MEM[last_K] = reg    # Registra o nome resultado na MEM

    print(MEM[K])