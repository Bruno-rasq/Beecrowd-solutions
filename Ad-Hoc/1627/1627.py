class Last_Hit:
    @staticmethod
    def who_gives_a_last_hit():
        AD, AT, BD, BT = [int(x) for x in input().split()]
        boss_life = int(input())
        
        currA = 0 
        currB = 0 
        time_sec = 0
        
        while True:
            if currA == time_sec: 
                boss_life -= AD
                currA += AT 
                if boss_life <= 0: return "Andre"
                
            if currB == time_sec:
                boss_life -= BD
                currB += BT
                if boss_life <= 0: return "Beto"
                
            time_sec += 1
            
n_tests = int(input())
for _ in range(n_tests):
    player = Last_Hit.who_gives_a_last_hit()
    print(player)