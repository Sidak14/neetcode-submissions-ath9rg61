class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        maxLength = 0
        rows, cols = len(matrix), len(matrix[0])

        def dfs(row, col):         
            if (row, col) in memo:
                return memo[(row, col)]
            
            currentVal = matrix[row][col]
            length = 1
            if row + 1 < rows and matrix[row + 1][col] > currentVal:
                length = max(length, 1 + dfs(row + 1, col))
            if row - 1 >= 0 and matrix[row - 1][col] > currentVal:
                length = max(length, 1 + dfs(row - 1, col))
            if col + 1 < cols and matrix[row][col + 1] > currentVal:
                length = max(length, 1 + dfs(row, col + 1))
            if col - 1 >= 0 and matrix[row][col - 1] > currentVal:
                length = max(length, 1 + dfs(row, col - 1))
            
            memo[(row, col)] = length
            return length

        for i in range(rows * cols):
            row = i // cols
            col = i % cols
            length = dfs(row, col)
            maxLength = max(maxLength, length)
        print(memo)
        return maxLength
            