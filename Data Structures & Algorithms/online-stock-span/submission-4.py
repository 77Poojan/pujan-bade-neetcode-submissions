class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        count = 1

        while self.stocks and self.stocks[-1][-1] <= price:
            prev_count, _ = self.stocks.pop()
            count += prev_count

        self.stocks.append((count, price))
        return count
    
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)