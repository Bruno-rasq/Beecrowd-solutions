class Lap:
    @staticmethod
    def laps_to_become_a_straggler(faster, slowest):
        diff = abs(slowest - faster)
        laps = 0
        while slowest > 0:
            laps += 1 
            slowest -= diff
            
        return laps
        
    @staticmethod
    def resolve():
        while True:
            try:
                faster, slowest = [int(x) for x in input().split()]
                laps = Lap.laps_to_become_a_straggler(faster, slowest)
                
                print(laps)
                
            except EOFError: break 
        
Lap.resolve()