E,G,F = [int(el) for el in input().split()]

E = E + G
count = 0

while E >= F:
    E = (E - F + 1)
    count = count + 1

print(count)