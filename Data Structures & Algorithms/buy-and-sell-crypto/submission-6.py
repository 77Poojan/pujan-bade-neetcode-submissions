class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        i, j = 0, 1
        maxx = 0

        for i in range(n):
            j = i + 1
            while j < n:
                if prices[i] < prices[j]:
                    maxx = max(maxx, prices[j] - prices[i])
                j += 1
        return maxx
