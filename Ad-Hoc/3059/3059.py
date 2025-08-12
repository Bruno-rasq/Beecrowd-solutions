class Pares_de_numeros:
    @staticmethod
    def solve(numeros, N, MIN, MAX):
        pares_validos = set()
        for i in range(N):
            curr = numeros[i]
            for j in range(i + 1, N):
                if MIN <= (curr + numeros[j]) <= MAX:
                    pares_validos.add((curr, numeros[j]))
                    
        print(len(pares_validos))
            
N, MIN, MAX = [int(x) for x in input().split()]
numeros = [int(x) for x in input().split()]

Pares_de_numeros.solve(numeros, N, MIN, MAX)