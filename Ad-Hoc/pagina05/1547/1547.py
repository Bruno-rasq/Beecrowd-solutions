camisetas_sortear = int(input())

for i in range(camisetas_sortear):
    alunos, numero_sorteado = [int(x) for x in input().split()]
    chutes = [int(x) for x in input().split()]
    
    chutes_aproximados = [abs(chute - numero_sorteado) for chute in chutes]
    indice_mais_proximo = chutes_aproximados.index(min(chutes_aproximados))
    print(indice_mais_proximo + 1)