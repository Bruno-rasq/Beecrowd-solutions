operation = input()

ROWS = 12
COLUMNS = 12

top_area = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0.0
element_count=0

for i in range(ROWS):
    for j in range(COLUMNS):
        current_number=float(input())
        if j in top_area:
            soma += current_number
            element_count += 1
    top_area = top_area[1:-1] #fatiamento

if operation == "S":
    print(f'{soma:.1f}')
else:
    print(f'{soma / element_count:.1f}')