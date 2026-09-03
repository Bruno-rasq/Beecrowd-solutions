# Entrada de funcionários por andar (do andar 1 ao 3)
andares = [int(input()) for _ in range(3)]

# Inicializar variável de melhor tempo com infinito
melhor_tempo = float('inf')

# Testar a máquina em cada um dos 3 andares
for i in range(3):
    tempo_total = 0
    for j in range(3):
        distancia = abs(i - j)
        tempo_total += andares[j] * 2 * distancia  # ida e volta
    melhor_tempo = min(melhor_tempo, tempo_total)

print(melhor_tempo)