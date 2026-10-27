class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append("#")
            grid.append(row)
     
        for i in range(m):
            grid[i][0] = "."
        for j in range(n):
            grid[m - 1][j] = "."
        
        result = []
        for i in range(m):
            row_str = "".join(grid[i])
            result.append(row_str)
            
        return result