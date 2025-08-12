class Assigning_Teams:
    @staticmethod
    def solve(source) -> None:
        teamA = source[1] + source[2]
        teamB = source[0] + source[3]
        
        diff = abs(teamB - teamA)
        print(diff)
        
        
skill_levels = sorted([int(x) for x in input().split()])
Assigning_Teams.solve(skill_levels)