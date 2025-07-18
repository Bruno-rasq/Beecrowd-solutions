class Sharing_with_Fink:
    @staticmethod
    def sharing(amount_food: int)-> None:
        woodpecker, fink, aux = 0, 0, 1
        
        while amount_food > 0:
            woodpecker += 1
            amount_food -= 1
            
            for _ in range(aux):
                if amount_food == 0:
                    fink += 1
                    woodpecker -= 1 
                    continue
                fink += 1
                amount_food -= 1 
                
            aux += 1 
            
        print(f"{fink} {woodpecker}")
            
    
    @staticmethod
    def resolve() -> None:
        while True:
            amount_food = int(input())
            if amount_food == 0: break 
        
            Sharing_with_Fink.sharing(amount_food)
            
Sharing_with_Fink.resolve()