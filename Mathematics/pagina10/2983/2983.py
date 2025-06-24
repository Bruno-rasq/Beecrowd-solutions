class Not_Everything_is_Strike:
    @staticmethod
    def is_prime(n):
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
        
    @staticmethod
    def resolve():
        
        n = int(input())
        memory = {} 
        primos = set()
        
        for _ in range(n):
            x = int(input())
            if x not in memory:
                res = Not_Everything_is_Strike.is_prime(x)
                memory[x] = True if res else False
                
            res = memory[x]
            if res: primos.add(x)
           
        print(len(primos))
        if len(primos) > 0:
            output = []
            for x in sorted(primos):
                output.append(str(x))
            format_out = ", ".join(output)
            print(f"{format_out}.")
        else: print()
            

Not_Everything_is_Strike.resolve()