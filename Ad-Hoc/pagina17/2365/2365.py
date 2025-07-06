from collections import defaultdict 
class Brazilian_Soccer_Big_Bet:
    @staticmethod
    def set_players(amount_players, amount_games):
        players = defaultdict(lambda: [0, []])
        
        for _ in range(amount_players):
            playes_name = input()
            for _ in range(amount_games):
                TA, PA, TB, PB = input().split()
                winner, loser, scoreboard = None, None, (PA, PB)
                
                if int(PA) > int(PB): winner, loser = TA, TB
                if int(PA) < int(PB): winner, loser = TB, TA
            
                players[playes_name][1].append([winner, loser, scoreboard])
                
        return players
        
    @staticmethod
    def set_score(bet, winner, loser, scoreboard):
        BW, BL, BSB = bet
        
        if BW == winner and BL == loser and (BSB[0] == scoreboard[0] and BSB[1] == scoreboard[1]): return 10
        elif BW == winner and BL == loser and (BSB[0] == scoreboard[0] or BSB[1] == scoreboard[1]): return 7
        elif BW == winner: return 5
        elif BW != winner and (BSB[0] == scoreboard[0] or BSB[1] == scoreboard[1]): return 2

        return 0
        
    @staticmethod
    def resolve():
        while True:
            amount_players, amount_games = [int(x) for x in input().split()]
            if amount_players == amount_games == 0: break
        
            players = Brazilian_Soccer_Big_Bet.set_players(amount_players, amount_games)
            
            for idx in range(amount_games): 
                TA, PA, TB, PB = input().split()
                scoreboard, winner, loser = (PA, PB), None, None
                if int(PA) > int(PB): winner, loser = TA, TB
                if int(PB) > int(PA): winner, loser = TB, TA
                
                for player in players:
                    bet = players[player][1][idx]
                    score = Brazilian_Soccer_Big_Bet.set_score(
                        bet, winner, loser, scoreboard
                    )
                    players[player][0] += score
                    
            scores = defaultdict(list)
            for player in players:
                score = players[player][0]
                scores[score].append(player)
                
            for score in sorted(scores, reverse=True):
                for player in sorted(scores[score]):
                    print(player, score)
                
Brazilian_Soccer_Big_Bet.resolve()