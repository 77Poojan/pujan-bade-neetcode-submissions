type FreqStack struct {
    frequency     map[int]int
    group         map[int][]int
    max_frequency int
}

func Constructor() FreqStack {
    return FreqStack{
        frequency:     make(map[int]int),
        group:         make(map[int][]int),
        max_frequency: 0,
    }
}

func (this *FreqStack) Push(val int) {
    this.frequency[val] += 1
    this.group[this.frequency[val]] = append(this.group[this.frequency[val]], val)
    this.max_frequency = max(this.max_frequency, this.frequency[val])
}

func (this *FreqStack) Pop() int {
    freq := this.max_frequency
    group := this.group

    val := group[freq][len(group[freq])-1]
    group[freq] = group[freq][:len(group[freq])-1]

    this.frequency[val]--

    if len(group[freq]) == 0 {
        this.max_frequency--
    }

    return val
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * obj := Constructor()
 * obj.Push(val)
 * param2 := obj.Pop()
 */
 