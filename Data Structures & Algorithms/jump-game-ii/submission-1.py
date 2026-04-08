class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [len(nums) + 1] * len(nums)
        jumps[0] = 0
        for i in range(len(nums)):
            end = min(i + nums[i] + 1, len(nums))
            for j in range(i + 1, end):
                jumps[j] = min(jumps[j], jumps[i] + 1)
        
        return jumps[-1]