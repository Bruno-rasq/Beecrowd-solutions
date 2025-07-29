from collections import defaultdict

class Tribol:
    gols_system = {
        "R": {"G": 2, "B": 1},
        "G": {"R": 1, "B": 2},
        "B": {"G": 1, "R": 2}
    }
    
    @staticmethod
    def get_result_game(scoring):
        
        teams = {"R": "red", "G": "green", "B": "blue"}
        
        for point in sorted(scoring, reverse=True):
            if len(scoring[point]) == 3: print("trempate"); return 
            if len(scoring[point]) == 2: print("empate"); return
            else:
                winner = scoring[point][0]
                print(teams[winner]); return
            
    
    @staticmethod
    def resolve():
        amount_games = int(input())
        for _ in range(amount_games):
            numbers_gols = int(input())
            teams = {"R": 0, "G": 0, "B": 0}
            
            for _ in range(numbers_gols):
                scoring_team, conceding_team = input().split()
                points = Tribol.gols_system[scoring_team][conceding_team]
                teams[scoring_team] += points
                
            scoring = defaultdict(list)
            scoring[teams["R"]].append("R")
            scoring[teams["G"]].append("G")
            scoring[teams["B"]].append("B")
            
            Tribol.get_result_game(scoring)
            
Tribol.resolve()