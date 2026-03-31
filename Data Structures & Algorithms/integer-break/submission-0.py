class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1 : 1}

        for i in range(2, n + 1):
            dp[i] = 0 if i == n else i
            for j in range(1, i):
                val = dp[j] * dp[i - j]
                dp[i] = max(dp[i], val) 
        
        return dp[n]
