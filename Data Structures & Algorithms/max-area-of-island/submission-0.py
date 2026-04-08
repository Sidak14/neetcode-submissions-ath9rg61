class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        for i in range(rows * cols):
            row = i // cols
            col = i % cols
            if not grid[row][col]:
                continue
            
            area = 0
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()

                if grid[row][col]:
                    area += 1

                grid[row][col] = 0
                if row - 1 >= 0 and grid[row - 1][col]:
                    stack.append((row - 1, col))
                if row + 1 < rows and grid[row + 1][col]:
                    stack.append((row + 1, col))
                if col - 1 >= 0 and grid[row][col - 1]:
                    stack.append((row, col - 1))
                if col + 1 < cols and grid[row][col + 1]:
                    stack.append((row, col + 1))
            
            maxArea = max(area, maxArea)
        
        return maxArea