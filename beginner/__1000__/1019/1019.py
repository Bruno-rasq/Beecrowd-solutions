num = int(input())

horas = num // 3600
minutos = (num % 3600) // 60
segundos = num % 60

print(f"{horas:.0f}:{minutos:.0f}:{segundos:.0f}")