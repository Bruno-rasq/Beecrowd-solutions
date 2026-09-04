class Distancia_entre_amigos:
    @staticmethod
    def solve():
        n = int(input())
        alturas = list(map(int, input().split()))

        max1 = float("-inf")  # para (A_i - i)
        max2 = float("-inf")  # para (A_i + i)
        ans = 0

        for j in range(n):
            # Caso 1: i < j -> usa max1
            ans = max(ans, max1 + alturas[j] + j)
            # Caso 2: i > j -> usa max2
            ans = max(ans, max2 + alturas[j] - j)

            # Atualiza máximos
            max1 = max(max1, alturas[j] - j)
            max2 = max(max2, alturas[j] + j)

        print(ans)
            
Distancia_entre_amigos.solve()