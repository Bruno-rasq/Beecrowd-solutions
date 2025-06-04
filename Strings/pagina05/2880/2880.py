
# Dada uma mensagem (string) e um crib (string), objetivo
# determinar quantas posicoes possiveis para o crib de maneira
# a dois caracteres não ficarem com o mesmo indice.

# exm: mensagem = "FDMLCRDMRALF", crib = "ARMADA"
# F D M L C R D M R A L F
# A R M A D A
#   A R M A D A -> sem sobreposição.
#     A R M A D A
#       A R M A D A -> sem sobreposição
#         A R M A D A
#           A R M A D A
#             A R M A D A

mensagem = input()
crib = input()

posicoes_possiveis = 0

for i in range((len(mensagem) - len(crib)) + 1):
    b = i
    contador = 0
    for j in range(len(crib)):
        
        if crib[j] == mensagem[b]: break
        b += 1
        contador += 1
        
    posicoes_possiveis +=  1 if contador == len(crib) else 0
    
print(posicoes_possiveis)
