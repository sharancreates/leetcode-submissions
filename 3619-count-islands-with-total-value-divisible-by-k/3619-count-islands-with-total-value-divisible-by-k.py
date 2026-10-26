class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] <= 0:
                return 0
            
            val = grid[r][c]
            grid[r][c] = 0 
            
            return val + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    total_value = dfs(r, c)
                    if total_value % k == 0:
                        island_count += 1
                        
        return island_count
