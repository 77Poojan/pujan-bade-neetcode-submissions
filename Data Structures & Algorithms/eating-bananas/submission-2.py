from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
 
        def check(k):
            hrs = 0
            for p in piles:
                hrs += ceil(p/k)
            return hrs <= h

        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else: 
                left = mid + 1
        return left  