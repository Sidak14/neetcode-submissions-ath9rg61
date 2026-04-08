class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [False] * len(nums)
        reachable[0] = True
        for i in range(len(nums)):
            if not reachable[i]:
                continue
            
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    break
                reachable[i + j] = True
        
        return reachable[-1]