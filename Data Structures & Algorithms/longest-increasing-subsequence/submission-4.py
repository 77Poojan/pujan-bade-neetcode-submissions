class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        n = len(nums)

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

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