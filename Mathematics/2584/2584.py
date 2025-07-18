#Area pentagono -> (1/4) * √5(5  + 2√5) * lado^2

import math

class Pentagon:
    @staticmethod
    def resolve():
        n = int(input())
        for _ in range(n):
            
            lado = int(input())
            
            Area_pentagon = (1/4) * (math.sqrt(5 * (5 + 2*math.sqrt(5)))) * lado**2
            
            print(f"{Area_pentagon:.3f}")
            
Pentagon.resolve()