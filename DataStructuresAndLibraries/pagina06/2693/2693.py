from  collections import defaultdict

# A ideia desta solucao é aplicar um bucket sort, metodo de
# ordenação que usa a estratégia de dividir e conquistar, assim
# dividindo os alunos primeiro por distancias onde cada balde 
# já ordenado possue subgrupos de dados, esses subgrupos sao 
# divididos em mais um balde desta vez por regiao, cada balde
# de regiao possue os nomes dos alunos e por fim basta ordenar
# os nomes.

while True:
    try:
        # Dicionário com buckets de distância -> buckets de região -> lista de nomes
        baldes = defaultdict(lambda: defaultdict(list))
        
        n = int(input())
        for _ in range (n):
            nome, regiao, distancia = input().split()
            baldes[int(distancia)][regiao].append(nome)
        
        # Itera ordenando por distância, região e nomes
        for distancia in sorted(baldes):
            for regiao in sorted(baldes[distancia]):
                for nome in sorted(baldes[distancia][regiao]):
                    print(nome)
                
    except EOFError: break
