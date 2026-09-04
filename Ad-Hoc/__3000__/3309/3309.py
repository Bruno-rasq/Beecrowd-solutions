def happy_number(n):
    return sum(int(x) ** 2 for x in str(n))

# Dicionário para armazenar resultados já calculados
memo = {}

def is_happy(n):
    visited = set()
    original = n

    while n != 1 and n not in visited:
        if n in memo:  # Se já sabemos o resultado desse número, reutilizamos
            memo[original] = memo[n]
            return memo[n]

        visited.add(n)
        n = happy_number(n)

    # Armazena o resultado para evitar repetir o cálculo no futuro
    result = (n == 1)
    for num in visited:
        memo[num] = result

    return result

# Entrada
n_digitos = int(input())
digitos = [int(x) for x in input().split()]

# Contagem de números felizes
count = sum(is_happy(num) for num in digitos)

print(count)