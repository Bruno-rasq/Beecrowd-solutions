from collections import defaultdict

class Solucao:
    def __init__(self):
        self.ranking = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
        self.processar_input()
        
    def processar_input(self):
        qnt_paises_competindo = int(input())
        for _ in range(qnt_paises_competindo):
            pais, ouro, prata, bronze = input().split()
            ouro, prata, bronze = int(ouro), int(prata), int(bronze)
            self.ranking[ouro][prata][bronze].append(pais)
    
    def ordenar_e_exibir_ranking(self):
        for ouro in sorted(self.ranking, reverse=True):
            for prata in sorted(self.ranking[ouro], reverse=True):
                for bronze in sorted(self.ranking[ouro][prata], reverse=True):
                    for pais in sorted(self.ranking[ouro][prata][bronze]):
                        print(pais, ouro, prata, bronze, sep=" ")
                        
                        
solucao = Solucao()
solucao.ordenar_e_exibir_ranking()