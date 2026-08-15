class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r =[0] * n, [0] * n
        l_wall = 0
        r_wall = 0
        count = 0

        for i in range(n):
            j = -i - 1
            l[i] = l_wall
            r[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        
        for i in range(n):
            pots = min(l[i], r[i])
            count += max(0, pots - height[i])
        
        return count
            