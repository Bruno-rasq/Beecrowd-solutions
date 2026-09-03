
# hash table + calculo de frequência.

tam_dicionario, funcionarios = [int(x) for x in input().split()]

dicionario = {}

for _ in range(tam_dicionario):
    palavra, valor = input().split()
    dicionario[palavra] = int(valor)
    
for _ in range(funcionarios):
    terminou = False
    valor_total = 0
    while not terminou:
        msg = input().split()
        if "." in msg: terminou = True
        for palavra in msg:
            if palavra in dicionario:
                valor_total += dicionario[palavra]
    
    print(valor_total)