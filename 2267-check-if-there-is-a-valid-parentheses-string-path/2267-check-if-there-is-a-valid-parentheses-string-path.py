class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
        
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
            
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        dp[0][0].add(1)
        
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                diff = 1 if grid[r][c] == '(' else -1
                
                possible_prev_balances = set()
                if r > 0:
                    possible_prev_balances.update(dp[r-1][c])
                if c > 0:
                    possible_prev_balances.update(dp[r][c-1])
                
                for bal in possible_prev_balances:
                    new_bal = bal + diff
                    if 0 <= new_bal <= (m + n) // 2:
                        dp[r][c].add(new_bal)
                        
        return 0 in dp[m-1][n-1]
