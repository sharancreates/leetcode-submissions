class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        next_R = [[None] * n for _ in range(m)]
        next_D = [[None] * n for _ in range(m)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    next_R[i][j] = (i, j)
                    next_D[i][j] = (i, j)
                else:
                    if i + 1 < m:
                        next_R[i][j] = next_D[i + 1][j]
                    else:
                        next_R[i][j] = None 
                    
                    if j + 1 < n:
                        next_D[i][j] = next_R[i][j + 1]
                    else:
                        next_D[i][j] = None # Out of bounds
        
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        
        dp[0][0][0] = 1 
        dp[0][0][1] = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                
                current_paths = (dp[i][j][0] + dp[i][j][1]) % MOD
                if current_paths == 0:
                    continue
                
                if j + 1 < n:
                    dest = next_R[i][j + 1]
                    if dest is not None:
                        r, c = dest
                        dp[r][c][0] = (dp[r][c][0] + current_paths) % MOD
                
                if i + 1 < m:
                    dest = next_D[i + 1][j]
                    if dest is not None:
                        r, c = dest
                        dp[r][c][1] = (dp[r][c][1] + current_paths) % MOD
     
        total_paths = (dp[m - 1][n - 1][0] + dp[m - 1][n - 1][1]) % MOD
        
        return (total_paths * 500000004) % MOD
