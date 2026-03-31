class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # hold = float('-inf')
        # sold = 0
        # rest = 0

        # for price in prices:
        #     prev_sold = sold
        #     sold = hold + price
        #     hold = max(hold, rest - price)
        #     rest = max(rest, prev_sold)

        # return max(sold, rest)

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                return max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                return max(sell, cooldown)

        return dfs(0, True)