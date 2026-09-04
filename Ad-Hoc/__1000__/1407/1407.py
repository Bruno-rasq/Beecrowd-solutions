class Weekend_Lottery:
    @staticmethod
    def least_drawn_numbers(number_of_draws: int, C: int, K: int):
        numbers = [0] * K  # frequências

        for _ in range(number_of_draws):
            draws = [int(x) for x in input().split()]
            for num in draws:
                numbers[num - 1] += 1

        MIN = min(numbers)
        LDN = [str(i + 1) for i in range(K) if numbers[i] == MIN]
        print(" ".join(LDN))


while True:
    ND, C, K = [int(x) for x in input().split()]
    if ND == C == K == 0:
        break
    Weekend_Lottery.least_drawn_numbers(ND, C, K)