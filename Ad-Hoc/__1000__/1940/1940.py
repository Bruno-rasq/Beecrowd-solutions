from collections import deque

class Strategy_Game:
    
    amount_playes, amount_rounds = [int(x) for x in input().split()]
    points = deque([int(x) for x in input().split()])
    players = {x: 0 for x in range(1, amount_playes + 1)}
    
    @staticmethod
    def resolve():
        max_points = -1
        winner = None
        while Strategy_Game.points:
            for idx in range(Strategy_Game.amount_playes):
                Strategy_Game.players[idx + 1] += Strategy_Game.points.popleft()
                if Strategy_Game.players[idx + 1] >= max_points:
                    winner = idx + 1
                    max_points = Strategy_Game.players[idx + 1]
                    
        print(winner)
        
Strategy_Game.resolve()