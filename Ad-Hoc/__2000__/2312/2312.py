
# uso uma adaptação da lógica de bucket sort,
# dividindo a llista em sublistas e ordenando-as simultaneamente.

from collections import defaultdict

qnt_nacoes_competindo = int(input())

ranking = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

for _ in range(qnt_nacoes_competindo):
    pais, ouro, prata, bronze = input().split()
    ranking[int(ouro)][int(prata)][int(bronze)].append(pais)
    
for ouro in sorted(ranking, reverse=True):
    for prata in sorted(ranking[ouro], reverse=True):
        for bronze in sorted(ranking[ouro][prata], reverse=True):
            for pais in sorted(ranking[ouro][prata][bronze]):
                print(pais, ouro, prata, bronze, sep=" ")