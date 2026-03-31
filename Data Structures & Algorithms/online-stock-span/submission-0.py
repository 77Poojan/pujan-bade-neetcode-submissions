class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        count= 1
        while self.stocks and self.stocks[-1][0] <= price:
            count += self.stocks[-1][1]
            self.stocks.pop()
        self.stocks.append((price, count))
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)