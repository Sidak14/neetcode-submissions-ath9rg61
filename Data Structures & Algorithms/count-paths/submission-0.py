class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1
        for i in range(m * n):
            row = i // n
            col = i % n
            if col + 1 < n:
                grid[row][col + 1] += grid[row][col]
            if row + 1 < m:
                grid[row + 1][col] += grid[row][col]
        
        return grid[-1][-1]