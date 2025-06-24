import math

# Os números que têm número ímpar de divisores são 
# exatamente os quadrados perfeitos
# 1^2, 2^2, 3^2, 4^2, ..., k^2 onde k = floor(√N)

# mqaior quadrado perfeito se dá √N 

class Xenlongao:
    @staticmethod
    def resolve():
        n = int(input())
        for _ in range(n):
        
            N = int(input())
            count = math.isqrt(N)
            print(N - count)
            
Xenlongao.resolve()