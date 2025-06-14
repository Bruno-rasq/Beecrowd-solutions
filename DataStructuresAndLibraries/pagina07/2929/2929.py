import sys

class Pilha:
    def __init__(self):
        self.pilha = []
        self.minimos = []

    def add(self, value):
        self.pilha.append(value)
        if not self.minimos or value <= self.minimos[-1]:
            self.minimos.append(value)

    def remove(self):
        if not self.pilha:
            return None
        valor = self.pilha.pop()
        if valor == self.minimos[-1]:
            self.minimos.pop()
        return valor

    def min(self):
        if not self.minimos:
            return None
        return self.minimos[-1]

input = sys.stdin.readline  # Leitura rápida
n = int(input())
pilha = Pilha()
saida = []  # Acumular resultados

for _ in range(n):
    linha = input()
    if linha.startswith("PUSH"):
        _, valor = linha.split()
        pilha.add(int(valor))
    elif linha.startswith("POP"):
        if pilha.remove() is None:
            saida.append("EMPTY")
    elif linha.startswith("MIN"):
        valor_min = pilha.min()
        saida.append("EMPTY" if valor_min is None else str(valor_min))

print('\n'.join(saida))