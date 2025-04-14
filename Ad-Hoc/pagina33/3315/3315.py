def converter_para_binario(n):
    binario = ""
    while n > 0:  
        binario += str(n % 2)
        n //= 2
    return binario[::-1] if binario else "0"

semanas = 4
mnv = 0 #maior_num_visuizacoes
for i in range(semanas):
    visualizacoes = [int(x) for x in input().split()]
    soma = 0
    for dia in range(7):
        soma += visualizacoes[dia]
    if soma > mnv:
        mnv = soma
        
print(f"{mnv} = {converter_para_binario(mnv)}")