from collections import defaultdict 

num_casos_teste = int(input())
for i in range(1, num_casos_teste + 1):
    
    qnt_renas, qnt_requisitada = [int(x) for x in input().split()]
    armazem = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    
    for _ in range(qnt_renas):
        nome, peso, idade, altura = input().split()
        altura = int(float(altura) * 100)
        armazem[int(peso)][int(idade)][altura].append(nome)
        
        
    fileira_renas_ordenadas = []
    for peso in sorted(armazem, reverse=True):
        for idade in sorted(armazem[peso]):
            for altura in sorted(armazem[peso][idade]):
                for nome in sorted(armazem[peso][idade][altura]):
                    fileira_renas_ordenadas.append(nome)
                    
    print(f"CENARIO {{{i}}}")
    for j in range(qnt_requisitada):
        print(f"{j + 1} - {fileira_renas_ordenadas[j]}")