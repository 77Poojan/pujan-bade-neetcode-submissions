class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j]) 
        return max(dp)

        
# from bisect import bisect_left
# from typing import List

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         tails = []

#         for n in nums:
#             i = bisect_left(tails, n)
#             if i == len(tails):
#                 tails.append(n)
#             else:
#                 tails[i] = n

#         return len(tails)