class Hashmat_the_Brave_Warrior:
    @staticmethod
    def solve():
        while True:
            try:
                n, m = [int(x) for x in input().split()]
                print(abs(n - m))
            except EOFError: break
        
Hashmat_the_Brave_Warrior.solve()