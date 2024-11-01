n= int(input())

index = 0
criancas = ["joao", "joao"]

for i in range(n - 1):
    criancas.append(f"crianca{i}")
    criancas.append(f"crianca{i}")

while len(criancas) > 1:
    index = (index + 28) % len(criancas)
    criancas.pop(index)

print("vai ganhar" criancas[0] == "joao" else "nao vai ganhar")