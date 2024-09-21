n = int(input())

cen = n // 100
rest100 = n % 100

cin = rest100 // 50
rest50 = rest100 % 50

vin = rest50 // 20
rest20 = rest50 % 20

dez = rest20 // 10
rest10 = rest20 % 10

cinco = rest10 // 5
rest5 = rest10 % 5

dois = rest5 // 2
rest2 = rest5 % 2

um = rest2

print(n)
print(f"{cen} nota(s) de R$ 100,00")
print(f"{cin} nota(s) de R$ 50,00")
print(f"{vin} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")