from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def check_k(k):
            hr = 0
            for p in piles:
                hr += ceil(p/k)
            return hr <= h

        while l < r:
            mid = l + (r - l) // 2
            if check_k(mid):
                r = mid
            else:
                l = mid + 1
    
        return l