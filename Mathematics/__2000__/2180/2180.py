def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

peso = int(input())
velocidade = 0
contador = 0

while contador < 10:
    if is_prime(peso):
        velocidade += peso
        contador += 1
    peso += 1

horas = 60000000 // velocidade
dias = horas // 24

print(f"{velocidade} km/h")
print(f"{horas} h / {dias} d")