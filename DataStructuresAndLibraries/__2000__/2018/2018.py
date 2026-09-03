from collections import defaultdict

class Solucao:
    def __init__ (self):
        #-> cada pais: [ouro, prata, bronze]
        self.quadro_medalhas = defaultdict(lambda: [0, 0, 0])
        self.ranking = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
                            
        self.set_medalhas()
        self.set_ranking()
        
    def set_medalhas(self):
        while True:
            try:
                modalidade = input()
                ouro, prata, bronze = input(), input(), input()
                
                self.quadro_medalhas[ouro][0] += 1
                self.quadro_medalhas[prata][1] += 1
                self.quadro_medalhas[bronze][2] += 1
            except EOFError: break
        
    def set_ranking(self):
        for pais in self.quadro_medalhas:
            ouro = self.quadro_medalhas[pais][0]
            prata = self.quadro_medalhas[pais][1]
            bronze = self.quadro_medalhas[pais][2]
            self.ranking[ouro][prata][bronze].append(pais)
      
    #-> bucket sort      
    def exibir_quadro_medalhistas(self):
        print("Quadro de Medalhas")
        for ouro in sorted(self.ranking, reverse=True):
            for prata in sorted(self.ranking[ouro], reverse=True):
                for bronze in sorted(self.ranking[ouro][prata], reverse=True):
                    for pais in sorted(self.ranking[ouro][prata][bronze]):
                        print(pais, ouro, prata, bronze, sep=" ")
    
    
sol = Solucao()
sol.exibir_quadro_medalhistas()