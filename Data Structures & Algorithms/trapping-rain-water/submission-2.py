class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_wall, r_wall = [0] * n, [0] * n
        l_max, r_max = 0, 0
        count = 0

        for i in range(n):
            j = -i - 1
            l_wall[i] = l_max
            r_wall[j] = r_max
            l_max = max(l_max, height[i])
            r_max = max(r_max, height[j])


        for i in range(n):
            pots = min(l_wall[i], r_wall[i]) 
            count += max(0, pots - height[i])
        
        return count