import math

def STLRF(fillet: str) -> None:
    parts = fillet.split('x')
    # primeiro e último fillets ficam inteiros
    max_size = max(len(parts[0]), len(parts[-1]))

    # internos são dobrados
    for mid in parts[1:-1]:
        max_size = max(max_size, math.ceil(len(mid) / 2))

    print(max_size)

while True:
    try:
        fillet = input()
        STLRF(fillet)
    except EOFError: break 