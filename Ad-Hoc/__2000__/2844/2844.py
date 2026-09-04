# Leitura dos dados de Matheus
Am, Rm, Em = map(int, input().split())

# Leitura dos dados de Vinicius
Av, Rv, Ev = map(int, input().split())

# Leitura da frase
S = input()

# Cálculo do tempo total de cada um
tempo_matheus = (Am * 2) + Rm + (Em * len(S))
tempo_vinicius = (Av * 2) + Rv + (Ev * len(S))

# Determina e imprime o vencedor
if tempo_matheus == tempo_vinicius:
    print("Empate")
elif tempo_matheus < tempo_vinicius:
    print("Matheus")
else:
    print("Vinicius")