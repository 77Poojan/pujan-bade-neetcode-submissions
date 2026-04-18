from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        def eat(hrs):
            count = 0
            for pile in piles:
                count += ceil(float(pile) / hrs)
            return count
            

        while left <= right:
            mid = (left + right) // 2
 
            if eat(mid) <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res