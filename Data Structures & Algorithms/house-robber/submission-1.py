class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)
            
        # best so far when stealing from house i
        bestSoFar = [nums[0], nums[1], nums[0] + nums[2]]
        for i in range(3, len(nums)):
            best = max(bestSoFar[i-3], bestSoFar[i - 2])
            # Can't steal from house i - 1.
            bestSoFar.append(best + nums[i])
        print(bestSoFar)
        return max(bestSoFar[-1], bestSoFar[-2])