# Problema: calcular o número de maneiras de descer uma escada de N degraus,
# podendo descer 1, 2 ou 3 degraus por vez (ou qualquer combinação deles).
# 
# Isso segue uma relação de recorrência semelhante à sequência de Tribonacci:
# f(n) = f(n-1) + f(n-2) + f(n-3)
# 
# A solução abaixo usa Programação Dinâmica (PD) com vetor para armazenar
# os subresultados e evitar recomputações. Também usa o módulo 10**9 + 7
# para evitar estouro de inteiros e atender às restrições do problema.

_MOD = 10**9 + 7
n_degrais = int(input())

def MDEND(n):
    if n == 0: return 1  # 1 forma de "não fazer nada"
    if n == 1: return 1  # apenas 1 degrau -> uma forma (1)
    if n == 2: return 2  # (1+1), (2)
    
    # Cria um vetor dp com n+1 posições inicializadas em 0
    dp = [0 for _ in range(n + 1)]
    dp[0], dp[1], dp[2] = 1, 1, 2   #casos base

    # Aplica a relação de recorrência:
    # dp[i] = dp[i-1] + dp[i-2] + dp[i-3], com módulo para evitar overflow
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % _MOD
        
    return dp[n]

print(MDEND(n_degrais))