class Estimating_the_Mean:
    @staticmethod
    def solve(n, notes):
        higher = max(notes)
        best = curr = 0
        
        for val in notes:
            if val == higher:
                curr += 1
                best = max(best, curr)
            else:
                curr = 0
                
        return best


n_test_cases = int(input())
for i in range(1, n_test_cases + 1):
    n = int(input())
    notes = [int(x) for x in input().split()]
    out = Estimating_the_Mean.solve(n, notes)
    print(f"Caso #{i}: {out}")