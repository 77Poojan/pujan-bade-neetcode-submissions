import math

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = left + ((right- left) // 2)
            sq = mid * mid
            if sq == x:
                return mid
            if sq < x:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1