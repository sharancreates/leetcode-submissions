class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')
        
        cost = [[INF] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                min_change = L
                
                for d in range(1, L):
                    if L % d == 0:
                        current_change = 0
                        m = L // d
                        for g in range(d):
                            left, right = 0, m - 1
                            while left < right:
                                if s[i + g + left * d] != s[i + g + right * d]:
                                    current_change += 1
                                left += 1
                                right -= 1
                        
                        if current_change < min_change:
                            min_change = current_change
                
                cost[i][j] = min_change
        
        dp = [INF] * n
        
        for j in range(1, n):
            dp[j] = cost[0][j]
            
        for w in range(2, k + 1):
            next_dp = [INF] * n
            for j in range(2 * w - 1, n):
                for p in range(2 * w - 3, j - 1):
                    if dp[p] != INF and cost[p + 1][j] != INF:
                        if dp[p] + cost[p + 1][j] < next_dp[j]:
                            next_dp[j] = dp[p] + cost[p + 1][j]
            dp = next_dp
            
        return dp[n - 1]
