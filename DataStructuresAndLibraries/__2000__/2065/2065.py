# Solução usa uma min-heap (fila de prioridade) com o módulo heapq.
# A heap armazena os caixas como tuplas: (tempo_livre, id_caixa, tempo_por_item),
# permitindo selecionar sempre o caixa que ficará livre primeiro (ou o de menor id em empate),
# simulando a dinâmica de atendimento da forma mais eficiente possível (O(log N) por operação).

import heapq

N, M = [int(x) for x in input().split()] #numero caixas e clientes

vi = [int(x) for x in input().split()]       # Tempo por item de cada caixa
clientes = [int(x) for x in input().split()] # Número de itens de cada cliente

# Inicializa a heap com todos os caixas livres no tempo 0
# Cada tupla: (tempo_livre, id_caixa, tempo_por_item)
caixas = [(0, i, vi[i]) for i in range(N)]
heapq.heapify(caixas)  # Transforma a lista em uma min-heap

ultimo_tempo = 0

for itens in clientes:
    # Pega o caixa que estará livre mais cedo (e com menor id em caso de empate)
    tempo_livre, id_caixa, tempo_item = heapq.heappop(caixas)
    
    # Calcula quando esse caixa ficará ocupado até
    novo_tempo = tempo_livre + tempo_item * itens
    
    # Reinsere o caixa na heap com o novo tempo de liberação
    heapq.heappush(caixas, (novo_tempo, id_caixa, tempo_item))
    
    # Atualiza o maior tempo de atendimento já registrado
    ultimo_tempo = max(ultimo_tempo, novo_tempo)

print(ultimo_tempo)