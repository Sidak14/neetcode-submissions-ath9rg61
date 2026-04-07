class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []

        def dfs(i, currentList, currentTotal):
            if currentTotal == target:
                output.append(currentList.copy())
                return
            if currentTotal > target or i >= len(candidates):
                return
            
            currentList.append(candidates[i])
            dfs(i+1, currentList, currentTotal + candidates[i])
            
            currentList.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            
            dfs(j, currentList, currentTotal)
        
        dfs(0, [], 0)
        return output