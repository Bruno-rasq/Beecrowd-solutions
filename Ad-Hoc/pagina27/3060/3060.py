# Entrada
V = int(input())  # Valor da compra
P = int(input())  # Número de parcelas

# Cálculo das parcelas
valor_base = V // P  # Parte inteira da divisão
resto = V % P  # Quantidade de parcelas que receberão +1

# Imprimindo as parcelas ajustadas
for i in range(P):
    if i < resto:
        print(valor_base + 1)  # As primeiras 'resto' parcelas recebem +1
    else:
        print(valor_base)  # As demais parcelas recebem o valor base