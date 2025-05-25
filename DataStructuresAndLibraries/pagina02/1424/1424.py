# Armazena posições (1-indexadas) de cada valor em um dicionário.
# Para cada consulta, retorna a posição da k-ésima ocorrência de um 
#valor, ou 0 se não existir.

while True:
    try:
        n, m = [int(x) for x in input().split()]
        lista = [int(x) for x in input().split()]
        
        hash_table = {}

        for i, valor in enumerate(lista):
            if valor not in hash_table:
                hash_table[valor] = []
            hash_table[valor].append(i + 1)

        for _ in range(m):
            k_ocorrencia, valor = [int(x) for x in input().split()]
            
            #lista de ocorrências
            LC = hash_table.get(valor, [])
            indice_desejado = k_ocorrencia - 1
            
            posicao = LC[indice_desejado] if indice_desejado < len(LC) else 0
            print(posicao)

    except EOFError: break 