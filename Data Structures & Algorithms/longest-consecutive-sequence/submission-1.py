class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxCount = 0
        for num in numsSet:
            if num - 1 in numsSet:
                continue
        
            count = 1
            nextNum = num + 1
            while nextNum in numsSet:
                count += 1
                nextNum += 1
            
            if count > maxCount:
                maxCount = count
        
        return maxCount