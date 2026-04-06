class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = -1
        l = 0
        r = len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if area > maxArea:
                maxArea = area
            
            if heights[l] < heights[r]:
                l += 1
                continue
            
            r -= 1
        
        return maxArea
            

        