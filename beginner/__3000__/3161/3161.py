n_frutas, n_lines = [int(x) for x in input().split()]

frutas = {input(): False for _ in range(n_frutas)}

for _ in range(n_lines):
    line = input().lower()
    for fruta in frutas:
        fruta_lower = fruta.lower()
        fruta_invertida = fruta_lower[::-1]
        if fruta_lower in line or fruta_invertida in line:
            frutas[fruta] = True

for fruta in frutas:
    print(
        f"Sheldon come a fruta {fruta.lower()}" if frutas[fruta] 
        else f"Sheldon detesta a fruta {fruta.lower()}"
    )