#A logica da questão consiste em achar um valor K minimo
#da diferença entre as somas dos elementos da lista.

#a ideia é fazer um loop N vezes e ir armazenando a diferença
#absoluta da somatoria de rangel - gugu, apos isso remover o 
#o primeiro elemento de gugu e passar para rangel. No fim do 
#processo haverá uma lista com as diferenças, pegar o menor valor.

# lista = [2, 3, 5]
# R = [] G = [2, 3, 5] -> diferença 10
# R = [2] G = [3, 5]   -> diferença 6
# R = [2, 3] G = [5]   -> diferença 0
# R = [2, 3, 5] G = [] -> diferença 10
#output = 0

while True:
    try:
        n = int(input())
        valores = [int(x) for x in input().split()]
        
        total = sum(valores)
        soma_rangel = 0
        menor_diferenca = float('inf')
        
        for i in range(n + 1):  # inclui caso Rangel faz todos
            soma_gugu = total - soma_rangel
            diff = abs(soma_rangel - soma_gugu)
            menor_diferenca = min(menor_diferenca, diff)
            
            if i < n:
                soma_rangel += valores[i]
        
        print(menor_diferenca)
        
    except EOFError: break