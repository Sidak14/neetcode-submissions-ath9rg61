class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times_to_reach = [((target - position[i]) / speed[i], position[i]) for i in range(len(position))]
        times_to_reach.sort(key = lambda x : (-x[1], x[0]))
        print(times_to_reach)

        stack = []
        for i in range(len(times_to_reach)):
            if stack and times_to_reach[i][0] <= stack[-1][0]:
                continue
            stack.append(times_to_reach[i])
        
        return len(stack)