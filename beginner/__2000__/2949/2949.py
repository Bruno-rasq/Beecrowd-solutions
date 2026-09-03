n = int(input())

hobbits = 0
anoes = 0
elfos = 0
humanos = 0
magos = 0

for _ in range(n):
    nome, raca = input().split()

    if raca == "X":
        hobbits += 1

    if raca == "H":
        humanos += 1

    if raca == "A":
        anoes += 1

    if raca == "E":
        elfos  += 1

    if raca == "M":
        magos += 1

print(f"{hobbist} Hobbit(s)")
print(f"{humanos} Humano(s)")
print(f"{elfos} Elfo(s)")
print(f"{anoes} Anao(oes)")
print(f"{magos} Mago(s)")