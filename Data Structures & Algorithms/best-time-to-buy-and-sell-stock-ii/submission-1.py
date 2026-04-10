class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        prev = prices[0]
        for price in prices[1:]:
            if prev < price:
                maxx += price - prev
            prev = price
        return maxx

        