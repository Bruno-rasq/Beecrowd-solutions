n = int(input())

meninos = 0
meninas = 0
for i in range(n):
    nome, sexo = input().split()

    if sexo == "M":
        meninos += 1
    else:
        meninas += 1

print(f"{meninos} carrinhos")
print(f"{meninas} bonecas")