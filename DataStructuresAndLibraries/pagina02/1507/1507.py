#Aplicando busca binaria em um algoritmo de busca de subsequencias. 

#aabccbba
# mapeamento = { "a": [0, 1, 7], "b": [2, 5, 6], "c": [3, 4] }

#consulta  "abc" pos = -1
# "a" -> bisect_right(mapeamento[a], pos) [0,1,7], -1 -> 0
# "b" -> bisect_right(mapeamento[b], pos) [2,5,6], 0 -> 2
# "c" -> bisect_right(mapeamento[c], pos) [3, 4], 2 -> 3
#subsequencia valida

#consulta  "abbc" pos = -1
# "a" -> bisect_right(mapeamento[a], pos) [0,1,7], -1 -> 0
# "b" -> bisect_right(mapeamento[b], pos) [2,5,6],  0 -> 2
# "b" -> bisect_right(mapeamento[b], pos) [5,6],    2 -> 5
# "c" -> bisect_right(mapeamento[c], pos) [3, 4],   5 ->  falha!
#subsequencia invalida:

def bisect_right(lista, valor):
    inicio, fim = 0, len(lista)
    while inicio < fim:
        meio = (inicio + fim) // 2
        if lista[meio] <= valor:
            inicio = meio + 1
        else:
            fim = meio
    return inicio
    

numero_casos_teste = int(input())
for _ in range(numero_casos_teste):
    
    mapeamento_char_indice = {}
    
    sequencia_atual = input()
    for ind, char in enumerate(sequencia_atual):
        if char not in mapeamento_char_indice:
            mapeamento_char_indice[char] = []
        mapeamento_char_indice[char].append(ind)
        
    numero_consultas = int(input())
    for _ in range(numero_consultas):
        consulta_atual = input()
        
        posicao_atual = -1
        subsequencia_valida = True
        
        for char in consulta_atual:
            if char not in mapeamento_char_indice:
                subsequencia_valida = False
                break
            
            lista_posicoes = mapeamento_char_indice[char]
            i = bisect_right(lista_posicoes, posicao_atual)
            
            if i == len(lista_posicoes):
                subsequencia_valida = False
                break
            
            posicao_atual = lista_posicoes[i]
            
        print("Yes" if subsequencia_valida else "No")