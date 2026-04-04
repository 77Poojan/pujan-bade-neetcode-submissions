class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # suffix sums
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        
        # dp[i][m] = max score current player can get from index i with M=m
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix[i]
                else:
                    for x in range(1, 2 * m + 1):
                        take = suffix[i] - dp[i + x][max(m, x)]
                        dp[i][m] = max(dp[i][m], take)
        
        return dp[0][1]
