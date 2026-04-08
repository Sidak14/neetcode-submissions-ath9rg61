class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = {}
        for time in times:
            u, v, t = time
            if u not in nodes:
                nodes[u] = []
            nodes[u].append((v, t))
        
        visited = [False] * n
        queue = []
        heapq.heappush(queue, (0, k))
        while queue:
            distance, node = heapq.heappop(queue)
            if visited[node - 1]:
                continue
            visited[node - 1] = True
            
            n -= 1
            if n == 0:
                return distance


            if node not in nodes:
                continue

            for edge in nodes[node]:
                nextNode, time = edge
                heapq.heappush(queue, (distance + time, nextNode))

        return -1