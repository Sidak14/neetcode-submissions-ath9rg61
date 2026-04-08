class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x < y:
                heapq.heappush(heap, x - y)
        
        if len(heap) == 1:
            return -1 * heapq.heappop(heap)
        
        return 0
