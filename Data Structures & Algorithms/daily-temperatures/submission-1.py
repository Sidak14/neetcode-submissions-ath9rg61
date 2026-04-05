class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack stores indices
        stack = []
        output = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp > temperatures[stack[-1]]:
                last = stack.pop()
                output[last] = i - last
            
            stack.append(i)
        
        return output