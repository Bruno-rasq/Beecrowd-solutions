import sys
import math
from functools import reduce

class Search_and_change:
    @staticmethod
    def resolve():
        # --------------------------------------------------------
        # Alguns casos de teste desta questão apresentam entradas
        # com quebras de linha inesperadas ou linhas em branco,
        # fazendo com que a leitura linha a linha falhe ou o 
        # programa pare prematuramente. Para contornar isso, o
        # código lê todos os números do input de uma vez,
        # ignorando quebras de linha, e processa os inteiros em
        # sequência, garantindo que todos os dados sejam lidos
        # na ordem correta mesmo com entradas mal formatadas.
        # --------------------------------------------------------
        
        data = list(map(int, sys.stdin.read().split()))
        idx = 0
        
        while idx < len(data):
            vector_size = data[idx]
            idx += 1
            queries = data[idx]
            idx += 1
            
            vetor = data[idx:idx+vector_size]
            idx += vector_size
            
            for _ in range(queries):
                requisited_op = data[idx]
                idx += 1
                
                if requisited_op == 1:
                    A = data[idx] - 1
                    idx += 1
                    B = data[idx]
                    idx += 1
                    V = data[idx]
                    idx += 1
                    
                    for i in range(A, B):
                        vetor[i] += V
                        
                elif requisited_op == 2:
                    A = data[idx] - 1
                    idx += 1
                    B = data[idx]
                    idx += 1
                    
                    start = A
                    end = B
                    
                    # Validar o intervalo para evitar lista vazia
                    if start < 0 or end > len(vetor) or start >= end:
                        print(0)
                        continue
                    
                    gcd = reduce(math.gcd, vetor[start:end])
                    print(gcd)

Search_and_change.resolve()