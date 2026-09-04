def somar_algarismos(n):
    digitos = [int(x) for x in str(n)]
    if len(digitos) == 1:
        return digitos[0]
    novo_valor = sum(digitos)
    return somar_algarismos(novo_valor)
    
while True:
    a, b = [int(x) for x in input().split()]
    if a == b == 0:
        break
    
    A = somar_algarismos(a)
    B = somar_algarismos(b)
    
    if A == B:
        print(0)
    else:
        print(1 if A > B else 2)