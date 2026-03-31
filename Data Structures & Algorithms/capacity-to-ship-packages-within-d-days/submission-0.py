class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left , right = max(weights), sum(weights)
        res = sum(weights)

        def canShip(k):
            currWeight = k 
            ships = 1
            for w in weights:
                if currWeight - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currWeight = k
                currWeight -= w
            return True

        while left <= right:
            mid = (left + right) // 2
            if canShip(mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res