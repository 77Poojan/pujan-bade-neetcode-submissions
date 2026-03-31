class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        invest = list(zip(capital, profits))
        heapq.heapify(invest)
        inhand = []


        for _ in range(k):
            while invest and invest[0][0] <= w:
                cp, profit = heapq.heappop(invest)
                heapq.heappush(inhand, -profit)
                
            if not inhand:
                break

            w += -heapq.heappop(inhand)
        
        return w