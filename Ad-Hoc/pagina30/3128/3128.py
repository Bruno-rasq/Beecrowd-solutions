idade_1 = int(input())
idade_2 = int(input())

condicao = (idade_1 >= 14 and idade_2 >= 14) or \
           (idade_1 >= 18 or idade_2 >= 18)

print("YES" if (idade_1 >= 6 and idade_2 >= 6 and condicao) else "NO")