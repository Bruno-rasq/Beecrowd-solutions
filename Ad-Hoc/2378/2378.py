data = [int(x) for x in input().split()]
QUANTIDADE_ACOES = data[0]
CAPACIDADE_MAXIMA = data[1]

carga = 0 
excedeu_capacidade = False

for _ in range(QUANTIDADE_ACOES):
    sairam, entraram = [int(x) for x in input().split()]
    
    carga = max(0, carga - sairam)
    carga += entraram
    if carga > CAPACIDADE_MAXIMA:
        excedeu_capacidade = True
        break 
    
print("S" if excedeu_capacidade else "N")