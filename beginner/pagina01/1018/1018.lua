local value = tonumber(io.read())
print(string.format("%.0f", value))

print(string.format("%d nota(s) de R$ 100,00", math.floor(value / 100)))
value = value % 100

print(string.format("%d nota(s) de R$ 50,00", math.floor(value / 50)))
value = value % 50

print(string.format("%d nota(s) de R$ 20,00", math.floor(value / 20)))
value = value % 20

print(string.format("%d nota(s) de R$ 10,00", math.floor(value / 10)))
value = value % 10

print(string.format("%d nota(s) de R$ 5,00", math.floor(value / 5)))
value = value % 5

print(string.format("%d nota(s) de R$ 2,00", math.floor(value / 2)))
value = value % 2

print(string.format("%d nota(s) de R$ 1,00", value))