class Solution:
    def climbStairs(self, n: int) -> int:
        output = [1, 1]
        while len(output) < n + 1:
            output.append(output[-1] + output[-2])
        
        return output[n]