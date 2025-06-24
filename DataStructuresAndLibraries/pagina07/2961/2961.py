class Solucao:
    @staticmethod
    def categorias_a_se_atentar():
        anos_registrados = int(input())
        categorias = [False for _ in range(4)]
        
        for i in range(anos_registrados):
            
            input() #-> key palpites
            palpites = []
            for _ in range(4): palpites.append(input())
            
            input() #-> key vencedores
            for j in range(4):
                if palpites[j].lower() == input().lower():
                    categorias[j] = True
            
        categorias_sem_acertos = [
            str(ind + 1) for ind, c in enumerate(categorias) if c == False]
            
        print(" ".join(categorias_sem_acertos))
            
Solucao().categorias_a_se_atentar()