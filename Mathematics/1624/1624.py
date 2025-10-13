from typing import List

class Solution:
    def knapsack_problem(self, itens: List[List[int]], capacity: int) -> int:
        dp = [[0] * (capacity + 1) for _ in range(len(itens) + 1)]
        
        for i in range(1, len(itens) + 1):
            curr_item_value, curr_item_weight = itens[i - 1][0], itens[i - 1][1]
            
            for j in range(capacity + 1):
                if j < curr_item_weight:
                    dp[i][j] = dp[i - 1][j]
                else:
                    remaining_capacity = j - curr_item_weight
                    added_value = dp[i - 1][remaining_capacity] + curr_item_value
                    dp[i][j] = max(dp[i - 1][j], added_value)
        return dp
        
while True:
    amount_itens = int(input())
    if amount_itens == 0:
        break 

    itens = []
    for _ in range(amount_itens):
        itens.append([int(x) for x in input().split()])

    capacity = int(input())
    dp = Solution().knapsack_problem(itens, capacity)
    
    print(dp[amount_itens][capacity])