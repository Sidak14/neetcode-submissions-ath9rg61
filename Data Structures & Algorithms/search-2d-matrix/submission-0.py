class Solution:
    def accessIndex(self, matrix: List[List[int]], index: int) -> int:
        n = len(matrix[0])
        row = index // n
        col = index % n
        return matrix[row][col]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m * n - 1
        while start <= end:
            mid = (start + end) // 2
            curr = self.accessIndex(matrix, mid)
            if curr == target:
                return True
            if curr < target:
                start = mid + 1
                continue
            end = mid - 1
        
        return False
