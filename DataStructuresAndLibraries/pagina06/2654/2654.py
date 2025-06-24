from collections import defaultdict

class Solucao:
    def __init__(self):
        #-> forca, abates, mortes, lista[nomes]
        self.campeoes = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
        self.qtd_campeoes = int(input())
        for _ in range(self.qtd_campeoes):
            nome, forca, abates, mortes = input().split()
            self.campeoes[int(forca)][int(abates)][int(mortes)].append(nome)
                        
    def campeao_mais_forte(self):
    
        max_fprca = max(self.campeoes)
        max_abates = max(self.campeoes[max_fprca])
        min_mortes = min(self.campeoes[max_fprca][max_abates])
        campeao = sorted(self.campeoes[max_fprca][max_abates][min_mortes])[0]
        print(campeao)
                        
                        
sol = Solucao()
sol.campeao_mais_forte()