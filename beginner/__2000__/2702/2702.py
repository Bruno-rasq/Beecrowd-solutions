#quantidade disponivel de frango, carne e macarrão 
frango, carne, macarrao = [int(x) for x in input().split()]

#quantidade de frango, carne, macarrão pedidos
pf, pc, pm = [int(x) for x in input().split()]

total = 0

total += (pf - frango) if pf > frango else 0
total += (pc - carne) if pc > carne else 0
total += (pm - macarrao) if pm > macarrao else 0

print(total)