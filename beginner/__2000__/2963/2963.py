candidatos = int(input())
votos = [int(input()) for _ in range(candidatos)]

maior_quantidade_votos = max(votos)

print("S" if votos[0] == maior_quantidade_votos else "N")