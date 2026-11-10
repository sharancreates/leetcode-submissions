class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs = [0] + costs
    
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  
        
        for i in range(1, n + 1):
            for k in range(1, 4):
                if i - k >= 0:
                    jump_cost = costs[i] + (k ** 2)
                    dp[i] = min(dp[i], dp[i - k] + jump_cost)
                    
        return dp[n]