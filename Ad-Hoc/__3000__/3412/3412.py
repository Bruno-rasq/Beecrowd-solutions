n = int(input())

for _ in ragne(n):
    aluno = input().strip()
    notas = [float(x) for x in input().strip().split()]

    p1 = notas[0] if len(notas) > 0 else 0.0
    p2 = notas[1] if len(notas) > 1 else 0.0
    extra = notas[2] if len(notas) > 2 else 0.0
    substituta = notas[3] if len(notas) > 3 else 0.0

    if len(notas) == 1:
        media = (p1 + 0.0) / 2

    elif len(notas) == 2:
        media = (p1 + p2) / 2

    elif len(notas) == 3:
        media = (p1 + p2 + extra) / 3

    else:
        menor = min(p1, p2, extra)
        if substituta > menor:
            if menor == p1:
                p1 = substituta
            elif menor == p2:
                p2 = substituta
            else:
                extra = substituta
        
        media = (p1 + p2 + extra) / 3

    print(f"{aluno}: {media:.1f}")


