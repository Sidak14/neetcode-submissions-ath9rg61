class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(index1, index2):
            if index1 >= len(text1) or index2 >= len(text2):
                return 0

            if (index1, index2) in memo:
                return memo[(index1, index2)]

            if text1[index1] == text2[index2]:
                memo[(index1, index2)] = 1 + dfs(index1 + 1, index2 + 1)
                return memo[(index1, index2)]
            
            memo[(index1, index2)] = max(dfs(index1 + 1, index2), dfs(index1, index2 + 1))
            return memo[(index1, index2)]

        return dfs(0, 0)
            