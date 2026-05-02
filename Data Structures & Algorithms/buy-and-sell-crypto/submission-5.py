class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx, i = 0, 0

        while i < len(prices):
            temp = prices[i]
            j = i + 1

            while (j < len(prices)) and temp < prices[j]:  
                maxx = max(maxx, prices[j] - prices[i])
                j += 1

            i += 1

        return maxx
