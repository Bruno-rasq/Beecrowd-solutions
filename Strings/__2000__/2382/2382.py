import math

largura, altura, profundidade, raio = map(int, input().split())

diagonal_caixa = math.sqrt(largura**2 + altura**2 + profundidade**2)
diametro_esfera = 2 * raio

print("S" if diagonal_caixa <= diametro_esfera else "N")