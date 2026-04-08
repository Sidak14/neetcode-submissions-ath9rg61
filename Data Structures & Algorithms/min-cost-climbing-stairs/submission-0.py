class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [0, 0]
        for i in range(2, len(cost)):
            print(mincost, i)
            curr = min(cost[i-2] + mincost[i-2], cost[i-1] + mincost[i-1])
            mincost.append(curr)
        print(mincost)
        
        return min(cost[-2] + mincost[-2], cost[-1] + mincost[-1])
