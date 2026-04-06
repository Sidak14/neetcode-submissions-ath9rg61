class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0 for _ in range(n)]
        maxLeft = 0
        for i in range(n):
            if height[i] > maxLeft:
                maxLeft = height[i]
            
            left[i] = maxLeft - height[i]
        
        print(left)

        right = [0 for _ in range(n)]
        maxRight = 0
        for i in range(n - 1, -1, -1):
            if height[i] > maxRight:
                maxRight = height[i]
            
            right[i] = maxRight - height[i]
        
        print(right)

        total = 0
        for i in range(n):
            total += min(left[i], right[i])

        return total
            

        