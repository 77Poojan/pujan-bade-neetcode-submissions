class Solution:
    def countBits(self, n: int) -> List[int]:
        # res = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     t = i
        #     while t:
        #         t = t & (t - 1)
        #         res[i] += 1
        # return res

        dp = [0] * (n + 1)

        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp
