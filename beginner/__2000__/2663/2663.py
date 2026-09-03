
def quicksort(arr):
    if len(arr) <= 1: return arr
    pivo = arr[len(arr) // 2]
    left = [x for x in arr if x > pivo] 
    middle = [x for x in arr if x == pivo]
    right = [x for x in arr if x < pivo]
    return quicksort(left) + middle + quicksort(right)

n_competidores = int(input())
n_vagas = int(input())

competidores = [int(input()) for _ in range(n_competidores)]

pontuacoes_ordenadas = quicksort(competidores)

# Pegamos a pontuação do último classificado
pontuacao_corte = pontuacoes_ordenadas[n_vagas - 1]

# Contamos todos com pontuação >= pontuação de corte
qnt_classificados = sum(1 for p in pontuacoes_ordenadas if p >= pontuacao_corte)

print(qnt_classificados)