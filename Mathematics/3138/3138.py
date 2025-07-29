import math
from collections import defaultdict 

class Tobias_Birthday:
    @staticmethod
    def resolve():
        n = int(input())
        ballons = defaultdict(int)
        total = 0
        
        for _ in range(n):
            ballon_color, amount = input().split()
            ballons[ballon_color] += int(amount)
            total += int(amount)
            

        denominador = 1
        for ballon in ballons:
            denominador *= math.factorial(ballons[ballon])
            
        print("Feliz aniversario Tobias!")
        print(math.factorial(total) // denominador)
            
        
Tobias_Birthday.resolve()