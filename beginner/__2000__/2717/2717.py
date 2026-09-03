minutos_faltam = int(input())
presenteA, presenteB = [int(x) for x in input().split()]

print("Farei hoje!" if (presenteA + presenteB) <= minutos_faltam else "Deixa para amanha!")