import sys

# Leitura da quantidade de consultas
N = int(sys.stdin.readline().strip())

consultas = []

# Leitura dos horários de cada consulta
for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    consultas.append((X, Y))

# Ordena as consultas pelo horário de término (Y)
consultas.sort(key=lambda x: x[1])

horario_final = 0
total_atendidas = 0

# Percorre as consultas escolhendo a melhor opção
for X, Y in consultas:
    if X >= horario_final:
        horario_final = Y  # Atualiza o horário final
        total_atendidas += 1

# Exibe o resultado
print(total_atendidas)