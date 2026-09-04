class Formula_1:
    @staticmethod
    def resolve():
        while True:
            n_granPrix, n_pilotos = [int(x) for x in input().split()]
            if n_granPrix == n_pilotos == 0: break
        
            gran_prixs = Formula_1.get_gran_prix_results(n_granPrix)
            n_ranking_systems = int(input())
            ranking_systems = Formula_1.get_ranking_systems(n_ranking_systems)
            
            for point_system in ranking_systems:
                ranking = {i: 0 for i in range(1, n_pilotos + 1)}
                
                for GP in gran_prixs:
                    for pilot in range(1, n_pilotos + 1):
                        posicao = GP[pilot - 1]
                        if posicao <= len(point_system):
                            ranking[pilot] += point_system[posicao - 1]
                
                # Depois de todos os GPs, printar o ranking final
                Formula_1.set_winner(ranking)
            
    @staticmethod #-> O(N)
    def get_gran_prix_results(n_granPrix):
        gran_prixs = []
        for _ in range(n_granPrix):
            result = [int(x) for x in input().split()]
            gran_prixs.append(result)
        return gran_prixs
        
    @staticmethod #-> O(M)
    def get_ranking_systems(n_systems):
        ranking_systems = []
        for _ in range(n_systems):
            n, *points = [int(x) for x in input().split()]
            ranking_systems.append(points)
        return ranking_systems
        
    @staticmethod #-> O(M)
    def set_winner(ranking):
        max_point = max(ranking.values())
        winners = []
        for pilot in ranking:
            if ranking[pilot] == max_point:
                winners.append(str(pilot))
            
        print(" ".join(winners))
        

Formula_1.resolve()