class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        suffix = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                continue
            
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        output = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]
        
        return output