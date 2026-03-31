class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices) 
        summ = 0
        i, j = 0, 1
        
        while j < n:
            if prices[j] > prices[i]:
                summ += prices[j]- prices[i] 
                i = j
                
            else:
                i += 1
            j += 1
        return summ
    

        