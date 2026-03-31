class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        l = 0
        for i in range(len(prices)):
            if prices[i] > prices[l]:
                maxx = max(maxx, prices[i] - prices[l])
            else:
                l = i
            
        return maxx