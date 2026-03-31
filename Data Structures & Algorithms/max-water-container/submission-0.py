class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxx = float("-inf")
        while i < j:
            l = min(heights[i], heights[j])
            b = j - i
            maxx = max(maxx, l * b)
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return maxx