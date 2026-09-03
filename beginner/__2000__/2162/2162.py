n = int(input())
dados = [int(x) for x in input().split()]

def padraoValePico(dados, n) -> bool:
    if n < 2:
        return False  # Se houver menos de 2 números, não pode haver padrão alternado
    
    for i in range(1, n):
        if (dados[i] > dados[i - 1] and (i == n - 1 or dados[i] > dados[i + 1])):  # Pico
            continue
        elif (dados[i] < dados[i - 1] and (i == n - 1 or dados[i] < dados[i + 1])):  # Vale
            continue
        else:
            return False  # Quebra o padrão
    
    return True

print("1" if padraoValePico(dados, n) else "0")