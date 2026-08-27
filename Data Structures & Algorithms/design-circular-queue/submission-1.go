type MyCircularQueue struct {
    data  []int
    head  int
    count int
    size  int
}


func Constructor(k int) MyCircularQueue {
    return MyCircularQueue{
        data: make([]int, k),
        head: 0,
        count: 0,
        size: k,
    }
}


func (this *MyCircularQueue) EnQueue(value int) bool {
    if this.IsFull() {
        return false
    }

    tail := (this.head + this.count) % this.size
    this.data[tail] = value
    this.count++
    return true
}


func (this *MyCircularQueue) DeQueue() bool {
    if this.IsEmpty() {
        return false
    }
    this.head = (this.head + 1) % this.size
    this.count--
    return true
}


func (this *MyCircularQueue) Front() int {
    if this.IsEmpty() {
        return -1
    }
    return this.data[this.head]
}


func (this *MyCircularQueue) Rear() int {
    if this.IsEmpty() {
        return -1
    }
    tail := (this.head + this.count - 1) % this.size
    return this.data[tail]
}


func (this *MyCircularQueue) IsEmpty() bool {
    return this.count == 0
}


func (this *MyCircularQueue) IsFull() bool {
    return this.count == this.size
}


/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * obj := Constructor(k);
 * param1 := obj.EnQueue(value);
 * param2 := obj.DeQueue();
 * param3 := obj.Front();
 * param4 := obj.Rear();
 * param5 := obj.IsEmpty();
 * param6 := obj.IsFull();
 */
 