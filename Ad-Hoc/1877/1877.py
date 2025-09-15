class Sansas_Snow_Castle:
    @staticmethod
    def is_consider_beautifull(N, towers, K):
        peaks = 0
        
        for i in range(1, N - 1):
            prev = towers[i - 1]
            curr = towers[i]
            next = towers[i + 1]
            
            if prev > curr < next: peaks += 1
            
            
        print("beautiful" if peaks == K else "ugly")
   
#Adicionei ao final uma torre extra com a altura máximo 
#para verificar se já uma vale no final do da sequência.
n, k = [int(x) for x in input().split()]
towers = [int(x) for x in input().split()] + [1000]   


Sansas_Snow_Castle.is_consider_beautifull(n + 1, towers, k)