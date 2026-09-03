teste = int(input())
cases = [int(x) for x in input().split()]

indice_queda = 0

for i in range(1, testes):
    if cases[i] < cases[i - 1]:
        indice_queda = i + 1
        break

print(indice_queda)