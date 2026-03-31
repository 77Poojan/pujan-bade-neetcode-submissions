class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summ = sum(stones)
        target = summ // 2
        dp = [0] * (target + 1)
        
        for s in stones:
            for t in range(target, s - 1, - 1):
                dp[t] = max(dp[t], dp[t - s] + s)
        
        return summ - 2 * dp[target]