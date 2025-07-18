class Game_of_Limit:
    
    @staticmethod
    def resolve():
        amount_cards, card_in_table, limit = [int(x) for x in input().split()]
        points = [0, 0]
        
        for idx in range(amount_cards - 1):
            card = int(input())
            if abs(card_in_table - card) <= limit:
                points[idx % 2] += abs(card_in_table - card)
                card_in_table = card
                
        print(f"{points[0]} {points[1]}")
    
Game_of_Limit.resolve()