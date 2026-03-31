class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numm = set(nums)
        maxx = 0

        for num in numm:
            if (num - 1) not in numm:
                l = 1
                while num + l in numm:
                    l += 1
                maxx = max(maxx, l)
        return maxx
            

