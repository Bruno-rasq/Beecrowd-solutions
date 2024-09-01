operation = input()

ROWS = 12
COLUMNS = 12
current_diagonal = 0
soma = 0.0
element_count=0

for i in range(ROWS):
    for j in range(COLUMNS):
        current_number=float(input())
        if j < current_diagonal:
            soma += current_number
            element_count += 1
    current_diagonal += 1

if operation == "S":
    print(f'{soma:.1f}')
else:
    print(f'{soma / element_count:.1f}')