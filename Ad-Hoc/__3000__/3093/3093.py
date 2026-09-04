class Guys_truco_1_0:
    @staticmethod
    def verify_superstition(cards):
        a, q, j, k = False, False, False, False
        for card in cards:
            if card == "J": j = True
            if card == "Q": q = True
            if card == "K": k = True
            if card == "A": a = True
            
        return a and q and j and k
        
rounds = int(input())

for _ in range(rounds):
    cards = input()
    
    response = Guys_truco_1_0.verify_superstition(cards)
    print("Aaah muleke" if response else "Ooo raca viu")

