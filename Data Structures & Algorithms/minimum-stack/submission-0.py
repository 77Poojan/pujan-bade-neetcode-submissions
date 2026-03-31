class MinStack:

    def __init__(self):
        self.s = []

        
    def push(self, val: int) -> None:
        self.s.append(val)
        return 


    def pop(self) -> None:
        self.s.pop()
        return


    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return min(self.s)
    