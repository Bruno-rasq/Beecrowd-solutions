#dado um valor N de base ABC devo converter para base 10
#para isso é necessário pegar o indice de cada caracter na tabela
#ASCII - 65, isso porque A em ASCII é 65 mas na base ABC é 0.

#tendo os valores da de cada caracter deve então converte para base 10
#resultado = (resultado * 26 + valor) % (10^9 + 7)

mod = (10**9) + 7

while True:
    try:
        n = input()
        
        resultado = 0
        for c in n:
            valor = ord(c) - ord('A')  # equivalente a -65
            resultado = (resultado * 26 + valor) % mod

        print(resultado)
        
    except EOFError:
        break