class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        nodes = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                nodes[i].append((distance, j))
                nodes[j].append((distance, i))
        
        totalCost = 0
        visited = set()
        minHeap = [(0, 0)]
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            totalCost += cost
            visited.add(node)
            for adjCost, adjNode in nodes[node]:
                if adjNode in visited:
                    continue
                heapq.heappush(minHeap, (adjCost, adjNode))
        
        return totalCost