data = [int(x) for x in input().split()]
QUANTIDADE_ESTACOES = data[0]
QUANTIDADE_COMANDOS = data[1]
ESTACAO_PROXIMA_DEVASTADA = data[2]
COMANDOS = [int(x) for x in input().split()]

registros = [0] * QUANTIDADE_ESTACOES
registros[0] += 1 
posicao_atual = 0

for comando in COMANDOS:
    posicao_atual = (posicao_atual + comando) % QUANTIDADE_ESTACOES
    registros[posicao_atual] += 1
    
qnt_vsz_robot_visitou_estacao_x = registros[ESTACAO_PROXIMA_DEVASTADA - 1]

print(qnt_vsz_robot_visitou_estacao_x)