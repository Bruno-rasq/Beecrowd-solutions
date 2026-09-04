data = [int(x) for x in input().split()]
QUANTIDADE_DE_PEDRAS = data[0] 
NUMERO_DE_SAPOS = data[1]

pedras = [False for _ in range(QUANTIDADE_DE_PEDRAS)]

for _ in range(NUMERO_DE_SAPOS):
    data = [int(x) for x in input().split()]
    tamanho_pulo = data[1]
    posicao_atual = data[0] - 1
    posicao_anterior = posicao_atual
    
    pedras[posicao_atual] = True
    
    while True:
        if (posicao_atual + tamanho_pulo) < QUANTIDADE_DE_PEDRAS:
            posicao_atual += tamanho_pulo
            pedras[posicao_atual] = True
        else: break 
    
    while True:
        if (posicao_anterior - tamanho_pulo) >= 0:
            posicao_anterior -= tamanho_pulo 
            pedras[posicao_anterior] = True
        else: break
    
    
for pedra in pedras: print(1 if pedra else 0)