operation = input()

ROWS = 12
COLUMNS = 12

x = 5
y = 6
inferior_area = list(range(x, y+1))

soma = 0.0
element_count=0

for i in range(ROWS):
    for j in range(COLUMNS):
        current_number=float(input())
        if(j < 5 and (i < 6 and j < i) or (i > 5 and j < 11 - i)):
            soma += current_number
            element_count += 1

if operation == "S":
    print(f'{soma:.1f}')
else:
    print(f'{soma / element_count:.1f}')