class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        if len(piles) == h:
            return maxPile
        
        low = 1
        high = maxPile
        while low < high:
            mid = (low + high) // 2
            time = 0
            for pile in piles:
                time += pile // mid
                if pile % mid != 0:
                    time += 1
            if time > h:
                low = mid + 1
                continue
            if time <= h:
                high = mid
        
        return (low + high) // 2