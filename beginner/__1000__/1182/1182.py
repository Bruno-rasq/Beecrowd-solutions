column = int(input())
operation = input()

ROWS = 12
COLUMNS = 12
current_column = 0
soma = 0.0
element_count = 0 

for i in range(ROWS):
    for j in range(COLUMNS):
        current_number = float(input())
        if j == column:
            soma += current_number
            element_count += 1  # Incrementa o contador de elementos

if operation == "S":
    print(f'{soma:.1f}')
else:
    print(f'{soma / element_count:.1f}')