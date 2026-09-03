from collections import defaultdict

class The_Champion:
    @staticmethod
    def solve(n: int):
        
        teams= defaultdict()
        for _ in range(n):
            team, team_score = input().split()
            teams[team] = int(team_score)
            
        for _ in range(n // 2):
            teamA, score, teamB = input().split()
            scoreA, scoreB = score.split("-")
            
            teams[teamA] += int(scoreA) * 3
            teams[teamB] += int(scoreB) * 3
            
            if scoreA == scoreB:
                teams[teamA] += 1
                teams[teamB] += 1
                
            elif int(scoreA) > int(scoreB): teams[teamA] += 5
            else: teams[teamB] += 5
            
                
        for team in sorted(teams.items(), key=lambda item: item[1], reverse=True):
            team_name, score = team 
            
            if team_name == "Sport":
                print(f"O Sport foi o campeao com {score} pontos :D")
                return
            
            print(f"O Sport nao foi o campeao. O time campeao foi o {team_name} com {score} pontos :(")
            return 
        
while True:
    n = int(input())
    if n == 0: break 

    The_Champion.solve(n)
    print()