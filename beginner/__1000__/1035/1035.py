A,B,C,D = [int(el) for el in input().split()]

condicao = (B > C and D > A and (C + D) > (A + B) and C >= 0 and D >= 0 and A % 2 == 0)

if condicao:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")