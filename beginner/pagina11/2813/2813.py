n = int(input())

guardachuvaCasa = 0
guardachuvatrabalho = 0
comprasCasa = 0
comprasTrabalho = 0

for _ in range(n):
    ida, volta = input().split()

    if ida == "chuva":
        if guardachuvaCasa > 0:
            guardachuvaCasa -= 1
        else:
            comprasCasa += 1
        guardachuvatrabalho += 1

    if volta == "chuva":
        if guardachuvatrabalho > 0:
            guardachuvatrabalho -= 1
        else:
            comprasTrabalho += 1
        guardachuvaCasa += 1

print(f"{comprasCasa} {comprasTrabalho}")