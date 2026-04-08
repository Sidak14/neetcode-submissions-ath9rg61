class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) <= 3:
            return max(nums)
            
        
        # best so far when stealing from house i
        bestSoFarWithFirst = [nums[0], nums[1], nums[0] + nums[2]]
        # Only go till second last
        for i in range(3, len(nums) - 1):
            best = max(bestSoFarWithFirst[i-3], bestSoFarWithFirst[i - 2])
            # Can't steal from house i - 1.
            bestSoFarWithFirst.append(best + nums[i])
        print(bestSoFarWithFirst)

        # Start from Second
        bestSoFarWithoutFirst = [0, nums[1], nums[2]]
        for i in range(3, len(nums)):
            best = max(bestSoFarWithoutFirst[i-3], bestSoFarWithoutFirst[i - 2])
            # Can't steal from house i - 1.
            bestSoFarWithoutFirst.append(best + nums[i])
        print(bestSoFarWithoutFirst)
        return max(bestSoFarWithFirst[-1], bestSoFarWithFirst[-2], bestSoFarWithoutFirst[-1])