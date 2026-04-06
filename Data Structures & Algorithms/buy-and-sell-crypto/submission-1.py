class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapestPrice = prices[0]
        maxProfit = 0
        for price in prices:
            cheapestPrice = min(price, cheapestPrice)
            profit = price - cheapestPrice
            maxProfit = max(profit, maxProfit)

        return maxProfit