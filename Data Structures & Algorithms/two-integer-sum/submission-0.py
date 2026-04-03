class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existingNums = {}
        for i in range(len(nums)):
            num = nums[i]
            if (target - num) in existingNums:
                return [existingNums[target - num], i]
            
            existingNums[num] = i
