volume_minimo, volume_maximo = 0, 100 #volume da TV

volume_inicial, quantidade_trocas = [int(x) for x in input().split()]
alteracoes_por_troca = [int(x) for x in input().split()]

volume_atual = volume_inicial
for i in range(quantidade_trocas):
    #Vnovo = max(0, min(100, Vatual + variacao))
    variacao = alteracoes_por_troca[i]
    novo_volume = max(0, min(100, volume_atual + variacao))
    volume_atual = novo_volume
    
print(volume_atual)


# VA = 50, delta = 14
# Vnovo = max(0, min(100, (50 + 14)))
# Vnovo = max(0, min(100, 64))
# Vnovo = max(0, 64)
# Vnovo = 64