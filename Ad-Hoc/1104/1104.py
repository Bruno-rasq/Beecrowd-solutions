class Exchanging_Cards:
    @staticmethod
    def resolve():
        while True:
            alice_num_cards, betty_num_cards = [int(x) for x in input().split()]
            if alice_num_cards == betty_num_cards == 0: break 
        
            set_cards_alice = set(input().split())
            set_cards_betty = set(input().split())
            
            unique_cards_alice = [card for card in set_cards_alice if card not in set_cards_betty]
            unique_cards_betty = [card for card in set_cards_betty if card not in set_cards_alice]
            
            asize = len(unique_cards_alice)
            bsize = len(unique_cards_betty)
            
            print(asize if asize < bsize else bsize) 

Exchanging_Cards.resolve()