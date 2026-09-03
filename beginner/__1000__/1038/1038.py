prices = [4.00, 4.50, 5.00, 2.00, 1.50]

code = int(input())
qnt = int(input())

valor = prices[code -1] * qnt

print(f"Total: R$ {valor:.2f}")