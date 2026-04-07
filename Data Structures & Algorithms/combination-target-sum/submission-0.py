class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        subset = []
        total = 0

        def dfs(index):
            nonlocal total
            if index >= len(nums):
                return
            
            subset.append(nums[index])
            total += nums[index]
            if total < target:
                dfs(index)
            elif total == target:
                output.append(subset.copy())
            
            total -= subset.pop()
            dfs(index + 1)
        
        dfs(0)
        return output