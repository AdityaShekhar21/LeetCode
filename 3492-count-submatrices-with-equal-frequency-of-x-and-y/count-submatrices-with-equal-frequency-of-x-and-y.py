class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Convert grid
        val = [[0]*n for _ in range(m)]
        hasX = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X':
                    val[i][j] = 1
                    hasX[i][j] = 1
                elif grid[i][j] == 'Y':
                    val[i][j] = -1
        
        # Prefix sums
        for i in range(m):
            for j in range(n):
                if i > 0:
                    val[i][j] += val[i-1][j]
                    hasX[i][j] += hasX[i-1][j]
                if j > 0:
                    val[i][j] += val[i][j-1]
                    hasX[i][j] += hasX[i][j-1]
                if i > 0 and j > 0:
                    val[i][j] -= val[i-1][j-1]
                    hasX[i][j] -= hasX[i-1][j-1]
        
        result = 0
        
        for i in range(m):
            for j in range(n):
                if val[i][j] == 0 and hasX[i][j] > 0:
                    result += 1
        
        return result