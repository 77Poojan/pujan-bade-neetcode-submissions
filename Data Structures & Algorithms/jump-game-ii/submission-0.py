class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        res = 0

        while r < n - 1:
            farthest = 0
            for j in range(l, r + 1):
               farthest = max(farthest, j + nums[j]) 
            
            l = r + 1
            r = farthest
            res += 1

        return res                
