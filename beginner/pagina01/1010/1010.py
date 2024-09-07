code1, qnt1, valor1 = input().split()
code2, qnt2, valor2 = input().split()

valor = (int(qnt1) * float(valor1)) + (int(qnt2) * float(valor2))

print(f"VALOR A PAGAR: R$ {valor:.2f}")