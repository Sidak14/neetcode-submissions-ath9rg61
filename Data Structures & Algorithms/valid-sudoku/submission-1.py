class Solution:
    def validateRule(self, subset: List[str]) -> bool:
        freq = {}
        for num in subset:
            if num == '.':
                continue
            
            if num not in freq:
                freq[num] = 0
            
            freq[num] += 1
            if freq[num] > 1:
                return False

        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            # Row
            if not self.validateRule(board[i]):
                return False

            # Column
            subset = []
            for j in range(len(board)):
                subset.append(board[j][i])
            if not self.validateRule(subset):
                return False
            
            # 3x3 Box
            row = i - i % 3
            col = (i % 3) * 3
            subset = [board[row][col], board[row][col + 1], board[row][col + 2],
                    board[row+1][col], board[row+1][col + 1], board[row+1][col + 2],
                    board[row+2][col], board[row+2][col + 1], board[row+2][col + 2]]
            if not self.validateRule(subset):
                return False

        return True    
            