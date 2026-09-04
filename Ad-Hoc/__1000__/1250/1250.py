class Kiloman:
    @staticmethod
    def n_times_KiloMan_is_hit():
        n_actions = int(input())
        hits = [int(x) for x in input().split()]
        actions = input()
        
        times_km_is_hit = 0
        for i in range(n_actions):
            height_hit = hits[i]
            curr_action = actions[i]
            
            if curr_action == 'S' and (height_hit == 1 or height_hit == 2):
                times_km_is_hit += 1
                continue
                
            if curr_action == 'J' and height_hit > 2:
                times_km_is_hit += 1
                continue
                
        print(times_km_is_hit)
        
n_test_cases = int(input())
for _ in range(n_test_cases):
    Kiloman.n_times_KiloMan_is_hit()