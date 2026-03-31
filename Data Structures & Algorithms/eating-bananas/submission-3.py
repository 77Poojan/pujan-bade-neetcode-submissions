from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def get_speed(t):
            count = 0
            for pile in piles:
                count += ceil(pile/t)
            return count

        while left <= right:
            mid = left + ((right - left) // 2)
            if get_speed(mid) <= h:
                right = mid - 1
            else:
                left = mid + 1
        
        return left