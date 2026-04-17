class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        stack = [0] * n
        
        for idx, height in enumerate(heights):
            stack[idx] = height
            j = idx + 1
            while j < n and height <= heights[j]:
                stack[idx] += height
                j += 1

            j = idx - 1
            while j >= 0 and height <= heights[j]:
                stack[idx] += height
                j -= 1
  
        return max(stack)   



            