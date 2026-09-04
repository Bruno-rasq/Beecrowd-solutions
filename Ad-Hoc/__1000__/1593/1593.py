qnt_casos = int(input())

for _ in range(qnt_casos):

    n = int(input())
    binario = ""
    bits_1 = 0
    
    while n > 0:
        resto = n % 2
        if resto == 1: bits_1 += 1
        binario = str(resto) + binario  # adiciona o bit à esquerda
        n = n // 2  # divisão inteira
    
    print(bits_1)