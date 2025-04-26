
def total_digitos(n):
    total = 0
    casas = [1_000_000, 100_000, 10_000, 1_000, 100, 10, 1]
    
    for casa in casas:
        if n >= casa:
            qtd = n - casa + 1
            digitos = len(str(casa))
            total += qtd * digitos
            n = casa - 1
    return total

n = int(input())
print(total_digitos(n))