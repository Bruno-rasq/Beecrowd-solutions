import math

class Etruscan_Warriors_Never_Play_Chess:
    @staticmethod
    def resolve():
        n = int(input())
        for _ in range(n):
            number_of_warrios = int(input())
            
            queues = (
                int((-1 + math.isqrt(1 + 8 * number_of_warrios))
                // 2)
            )
            print(queues)
            
Etruscan_Warriors_Never_Play_Chess.resolve()