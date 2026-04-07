class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        output = []

        def dfs(i, subset):
            if i >= len(nums):
                output.append(subset.copy())
                return subset
            
            subset.append(nums[i])
            dfs(i + 1, subset)

            subset.pop()
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1

            dfs(j, subset)
        
        dfs(0, [])
        return output