type entry struct {
    price int
    count int
}

type StockSpanner struct {
    stack []entry
}

func Constructor() StockSpanner {
    return StockSpanner{stack: []entry{}}
}

func (this *StockSpanner) Next(price int) int {
    count := 1

    for len(this.stack) > 0 && this.stack[len(this.stack) - 1].price <= price {
        last := this.stack[len(this.stack) - 1]
        this.stack = this.stack[:len(this.stack) - 1]
        count += last.count
    }

    this.stack = append(this.stack, entry{price, count})
    return count
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor()
 * param1 := obj.Next(price)
 */
 