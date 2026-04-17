class FreqStack:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.group = defaultdict(list)
        self.max_frequency = 0
      
    def push(self, val: int) -> None:
        self.frequency[val] += 1
        self.max_frequency = max(self.max_frequency, self.frequency[val])
        self.group[self.frequency[val]].append(val)

    def pop(self) -> int:
        val = self.group[self.max_frequency].pop()
        self.frequency[val] -= 1

        if not self.group[self.max_frequency]:
            self.max_frequency -= 1
        
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()