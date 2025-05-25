#O problema se trata de um grafo direcionado com busca em largura (DFS)
#a DFS vai percorrer todos os nós do gráfico e seus vizinhos 
#armazenando-os em um Set (visitados). Apartir dos visitados
#é possível descobrir quais nós (ruas) não são alcançáveis.

#para encontrar os nós (ruas) onde ficaria preso na cidade sem
#conseguir voltar a rodoviária circular (ponto 0) basta inverter
#o grafo e novamente usar o DFS, sendo os resultados aqueles visitados
#que nao conseguem chegar ao ponto 0.


def DFS(grafo, inicio, visitado):
    stack = [inicio]
    while stack:
        atual = stack.pop()
        if atual not in visitado:
            visitado.add(atual)
            stack.extend(grafo[atual])

N_RUAS = int(input())

mapa_ruas = {}
ordem_entrada = []

for _ in range(N_RUAS):
    ID, qnt_ruas, *ruas = map(int, input().split())
    mapa_ruas[ID] = ruas
    ordem_entrada.append(ID)

grafo_reverso = {rua: [] for rua in mapa_ruas}
for rua, vizinhos in mapa_ruas.items():
    for vizinho in vizinhos:
        grafo_reverso[vizinho].append(rua)

visitados = set()
alcancam_zero = set()

DFS(mapa_ruas, 0, visitados)
DFS(grafo_reverso, 0, alcancam_zero)

unreachable = {rua for rua in mapa_ruas if rua not in visitados}
trapped = {rua for rua in mapa_ruas if rua != 0 and rua not in alcancam_zero}

problemas = False

for rua in ordem_entrada:
    if rua in trapped:
        print(f'TRAPPED {rua}')
        problemas = True

for rua in ordem_entrada:
    if rua in unreachable:
        print(f'UNREACHABLE {rua}')
        problemas = True

if not problemas:
    print('NO PROBLEMS')