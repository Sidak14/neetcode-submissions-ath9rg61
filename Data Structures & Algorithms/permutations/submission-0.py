class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        selected = [False] * len(nums)

        def dfs(currentList, selected):
            if len(currentList) == len(nums):
                output.append(currentList.copy())
                return
            
            for i in range(len(selected)):
                if selected[i]:
                    continue
                
                selected[i] = True
                currentList.append(nums[i])
                dfs(currentList, selected)

                selected[i] = False
                currentList.pop()
            
        dfs([], selected)
        return output