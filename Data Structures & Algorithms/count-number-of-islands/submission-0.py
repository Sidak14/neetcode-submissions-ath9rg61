class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        m, n = len(grid), len(grid[0])
        for i in range(m * n):
            row = i // n
            col = i % n
            if grid[row][col] == "0":
                continue
            
            numIslands += 1
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()
                grid[row][col] = "0"
                if row > 0 and grid[row - 1][col] == "1":
                    stack.append((row - 1, col))
                if  row < m - 1 and grid[row + 1][col] == "1":
                    stack.append((row + 1, col))
                if col > 0 and grid[row][col - 1] == "1":
                    stack.append((row, col - 1))
                if col < n - 1 and grid[row][col + 1] == "1":
                    stack.append((row, col + 1))
        
        return numIslands