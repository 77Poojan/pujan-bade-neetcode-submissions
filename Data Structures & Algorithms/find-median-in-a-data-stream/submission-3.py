import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []


    def addNum(self, num: int) -> None:
        if self.small and -self.small[0] > num:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        if len(self.small) > len(self.large) + 1:
            n = -heapq.heappop(self.small)
            heapq.heappush(self.large, n)

        if len(self.small) + 1 < len(self.large):
            n = heapq.heappop(self.large)
            heapq.heappush(self.small, -n)


    def findMedian(self) -> float:
        s = len(self.small)
        l = len(self.large)

        if s > l:
            return -self.small[0]
        
        elif s < l:
            return self.large[0]
        
        return (-self.small[0] + self.large[0])/ 2.0