class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0

        for idx, height in enumerate(heights):
            start = idx
            while stack and  stack[-1][0] > height:
                h, i = stack.pop()
                maxArea = max(maxArea, h * (idx - i))
                start = i
            stack.append((height, start))
                
        while stack:
            h, i = stack.pop()
            maxArea = max(maxArea, h * (n -i))
        return maxArea




            