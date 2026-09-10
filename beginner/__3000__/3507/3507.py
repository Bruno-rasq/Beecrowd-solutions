N = int(input())    # numero de animais
M = int(input())    # numero de patas

# M = (2 * G) + (4 * T)
# G == numero de gansos
# T == numero de tigres

# ENCONTRA O VALOR DE G ou T para termos apenas
# UMA VARIAVEL NA EQUAÇÃO.
# N = G + T 
# N - G = T
# N - T = G

# ENCONTRA O NUMERO DE GANSOS.
# M = (2 * G) + (4 * (N - G))
# M = 2G + 4N - 4G
# M - 4N = 2G - 4G
# G = |M|
G = int(abs((M - 4*N) / -2))

# ENCONTRA O NUMERO DE TIGRES.
# M = (2 * Gansos) * (4 * T)
# M / (2*G) = 4T
# T = |M|
T = int(abs((M - 2*G) / 4))

print(T)
print(G)