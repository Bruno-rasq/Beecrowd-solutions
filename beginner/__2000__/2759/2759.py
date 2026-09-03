a = input()
b = input()
c = input()

index = 0
data = [a, b, c]

for _ in range(3):
    A = data[index]
    B = data[(index + 1) % len(data)]
    C = data[(index + 2) % len(data)]
    print(f"A = {A}, B = {B}, C = {C}")
    index = (index + 1) % lne(data)