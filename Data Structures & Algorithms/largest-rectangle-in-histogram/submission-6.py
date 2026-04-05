class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [0 for i in range(len(heights))]
        stack = []
        for i in range(len(heights)):
            if not stack or heights[stack[-1]] < heights[i]:
                stack.append(i)
                continue
            
            # heights[[stack][-1]] >= heights[i]
            leftmost = stack.pop()
            while stack and heights[stack[-1]] >= heights[i]:
                leftmost = stack.pop()
            
            left[i] = left[leftmost] + (i - leftmost)
            stack.append(i)

        right = [0 for i in range(len(heights))]
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            if not stack or heights[stack[-1]] < heights[i]:
                stack.append(i)
                continue
            
            # heights[[stack][-1]] >= heights[i]
            rightmost = stack.pop()
            while stack and heights[stack[-1]] >= heights[i]:
                rightmost = stack.pop()
            
            right[i] = right[rightmost] + (rightmost - i)
            stack.append(i)
        
        
        maxArea = -1
        for i in range(len(heights)):
            height = heights[i]
            width = left[i] + right[i] + 1
            area = width * height
            if area > maxArea:
                maxArea = area
            
        return maxArea