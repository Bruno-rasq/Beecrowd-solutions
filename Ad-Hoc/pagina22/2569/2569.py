valorA, operacao, valorB = input().split()

A = int(valorA.replace("7", "0"))
B = int(valorB.replace("7", "0"))

def exibirResultado(resultado):
    return int(str(resultado).replace("7", "0"))
   
print(
    exibirResultado(A + B) 
    if operacao == "+" 
    else exibirResultado(A * B)
    )