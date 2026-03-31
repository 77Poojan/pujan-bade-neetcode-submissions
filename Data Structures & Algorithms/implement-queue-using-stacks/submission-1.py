class MyQueue:

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)


    def pop(self) -> int:
        q = self.queue
        r = q[0]
        q.remove(r)
        return r
        
        
    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return True if not self.queue else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()