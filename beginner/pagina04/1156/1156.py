a = 3
b = 2

result = 1 + (a / b)
while a <= 39:
  a += 2
  b *= 2
  result += (a / b)

print(f"{result:.2f}")