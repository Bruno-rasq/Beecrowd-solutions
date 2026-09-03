
#sequencia binaria + sliding window

#O problema consiste em identificar a maior sequência de lampadas
#queimadas em um conjunto, cada um do N conjuntos é dado por hm valor
#na base 10 que ao ser convertido para base 2 forma a sequência de
#lampadas.

#1 para lampadas quebradas, 0 para lampadas funcionando.

#def base_2(n):   #O(log2n)
    #if n == 0: return "0"
    
    #binario = ""
    #while n > 0:
        #resto = n % 2
        #binario = str(resto) + binario
        #n = n // 2
    #return binario


n = int(input()) # 1 <= n <= 10^3
for _ in range(n):
    
    base_10 = int(input())
    _binary = bin(base_10)[2:] #converte base 10/ base 2 e remove o prefixo 'ob'
    
    #sliding window
    maior_sequencia = 0
    atual = 0
    for _bin in _binary:
        if _bin == "1":
            atual += 1
            maior_sequencia = max(maior_sequencia, atual)
        else:
            atual = 0
        
    print(maior_sequencia)