class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxx = 0

        while i < j:
            if heights[i] < heights[j]:
                maxx = max(maxx, heights[i] * (j - i))
                i += 1
            else:
                maxx = max(maxx, heights[j] * (j - i))
                j -= 1

        return maxx