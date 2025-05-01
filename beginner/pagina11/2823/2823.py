n = int(input())
processos = [[int(x) for x in input().split()] for _ in range(n)]

quos = [dado[0]/dado[1] for dado in processos]
sigma = sum(quo for quo in quos)

print("OK" if sigma <= 1.0 else "FAIL")