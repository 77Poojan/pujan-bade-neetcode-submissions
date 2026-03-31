class Solution:
    def trap(self, height: List[int]) -> int:
        lwall, rwall = 0, 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        count = 0

        for i in range(n):
            j = -i-1
            max_left[i] = lwall
            max_right[j] = rwall
            lwall = max(height[i], lwall)
            rwall = max(height[j], rwall)
        
        for j in range(n):
            pot = min(max_left[j], max_right[j])
            count += max(0, pot-height[j])
        
        return count     
