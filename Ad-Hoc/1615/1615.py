def greater_than_50(votes, M):
    return votes > M // 2   # mais claro e direto

class Insatisfaction_on_Elections:
    @staticmethod
    def winning_candidate(N, M):
        candidates = [0] * N
        votes = [int(x) for x in input().split()]

        for v in votes:
            candidates[v - 1] += 1

        # pega o candidato com mais votos
        max_votes = max(candidates)
        winner = candidates.index(max_votes) + 1

        if greater_than_50(max_votes, M):
            return winner
        return -1
        
teste_cases = int(input())
for _ in range(teste_cases):
    N, M = [int(x) for x in input().split()]
    out = Insatisfaction_on_Elections.winning_candidate(N, M)
    print(out)