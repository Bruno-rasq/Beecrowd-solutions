n1, n2, n3, n4 = [float(n) for n in input().split()]

def calcularMedia(n1, n2, n3, n4):
    return ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

media = calcularMedia(n1, n2, n3, n4)

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    exame = float(input())

    print("Aluno em exame.")
    print(f"Nota do exame: {exame}")

    mediaComExame = (media + exame) / 2

    if mediaComExame >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {mediaComExame}")