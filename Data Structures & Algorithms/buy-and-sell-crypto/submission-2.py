class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        temp = prices[0]

        for i in range(1, len(prices)):
            if temp < prices[i]:
                maxx = max(maxx, prices[i] - temp)
            else:
                temp = prices[i]
        return maxx