MOD = 10**9 + 7

class The_Note:
    @staticmethod
    def resolve():
        while True:
            try:
                N, K = [int(x) for x in input().split()]
                
                notas = []
                for _ in range(N):
                    notas.append(int(input()))
                
                # Pegamos as K maiores
                notas.sort(reverse=True)
                print(sum(notas[:K]) % MOD)
            except EOFError: break

The_Note.resolve()