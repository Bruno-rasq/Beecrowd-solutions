class Rangel_and_the_Array_Game_I:
    @staticmethod
    def frequence(array, kth):
        freq = 0 
        for n in array:
            if n == kth: freq += 1 
        return freq
    
    @staticmethod
    def resolve():
        length_array, amount_queries = [int(x) for x in input().split()]
        array = [int(x) for x in input().split()]
        
        for _ in range(amount_queries):
            left, right, kth, G, D = [int(x) for x in input().split()]
            
            interval = sorted(array[left - 1: right])
            k = interval[kth - 1]
            
            kth_freq = Rangel_and_the_Array_Game_I.frequence(interval, k)
            
            out = f"{k} {kth_freq}"
            
            g_dist, d_dist = abs(kth_freq - G), abs(kth_freq - D)
            
            if g_dist < d_dist: out += " G"
            if g_dist > d_dist: out += " D"
            if g_dist == d_dist: out += " E"
            
            print(out)
            
            
            
Rangel_and_the_Array_Game_I.resolve()