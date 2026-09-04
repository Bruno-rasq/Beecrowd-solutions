n = int(input())

for _ in range(n):
    equacao = input().split()
    A = int(equacao[0])
    B = int(equacao[2])
    C = int(equacao[4])
    operador = equacao[1]
    
    if operador == "+":
        resultado = A + B
    elif operador == "-":
        resultado = A - B
    elif operador == "x":  # CORRIGIDO
        resultado = A * B
        
    if C != resultado:
        errou = abs(C - resultado)
        print(f"E{'r' * errou}ou!")