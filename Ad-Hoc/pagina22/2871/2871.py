class Coffee_Harvest:
    @staticmethod
    def resolve():
        while True:
            try:
                m, n = [int(x) for x in input().split()]
                
                grains = 0
                for _ in range(m):
                    grains += sum([int(x) for x in input().split()])
                    
                sacks = (grains // 60) if grains >= 60 else 0
                leftover_grains = grains - (60 * sacks)
                
                print(f"{sacks} saca(s) e {leftover_grains} litro(s)")
            
            except EOFError: break
    
Coffee_Harvest.resolve()