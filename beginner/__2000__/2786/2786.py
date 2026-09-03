l = int(input()) #largura
c = int(input()) #comprimento

azulejos_tipo_1 = (c * l) + ((c - 1) * (l - 1))
azulejos_tipo_2 = ((l - 1) * 2) + ((c - 1) * 2)

print(azulejos_tipo_1)
print(azulejos_tipo_2)