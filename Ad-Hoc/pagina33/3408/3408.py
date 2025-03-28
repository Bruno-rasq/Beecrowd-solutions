n = int(input())
soma = 0

for _ in range(n):
    digitos = "".join([char for char in input() if char.isdigit()])
    soma += int(digitos)
    
print(soma)