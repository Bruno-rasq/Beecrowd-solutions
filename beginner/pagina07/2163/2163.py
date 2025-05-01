N, M = [int(x) for x in input().split()]

celula = []
for _ in range(N):
    celula.append([int(x) for x in input().split()])

encontrado = False

for i in range(1, N - 1):
    for j in range(1, M - 1):
        if celula[i][j] == 42:
            if (celula[i - 1][j - 1] == 7 and
                celula[i - 1][j] == 7 and
                celula[i - 1][j + 1] == 7 and
                celula[i][j - 1] == 7 and
                celula[i][j + 1] == 7 and
                celula[i + 1][j - 1] == 7 and
                celula[i + 1][j] == 7 and
                celula[i + 1][j + 1] == 7):
                print(f"{i + 1} {j + 1}")  # posições iniciam em 1
                encontrado = True
                break
    if encontrado:
        break

if not encontrado:
    print("0 0")