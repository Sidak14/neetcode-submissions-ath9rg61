class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # minHeap = [(currentTime, row, col)]
        minHeap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        while minHeap:
            currentTime, row, col = heapq.heappop(minHeap)
            if (row, col) == (n - 1, n - 1):
                return currentTime

            if visited[row][col]:
                continue
            visited[row][col] = True
            
            if row - 1 >= 0 and not visited[row - 1][col]:
                time = max(currentTime, grid[row - 1][col])
                heapq.heappush(minHeap, (time, row - 1, col))
            
            if row + 1 < n and not visited[row + 1][col]:
                time = max(currentTime, grid[row + 1][col])
                heapq.heappush(minHeap, (time, row + 1, col))

            if col - 1 >= 0 and not visited[row][col - 1]:
                time = max(currentTime, grid[row][col - 1])
                heapq.heappush(minHeap, (time, row, col - 1))

            if col + 1 < n and not visited[row][col + 1]:
                time = max(currentTime, grid[row][col + 1])
                heapq.heappush(minHeap, (time, row, col + 1))
        
