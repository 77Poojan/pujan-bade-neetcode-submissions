class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:        
        left = max(weights)
        right = sum(weights)
   
        def canShip(max_weight):
            curr_capacity = max_weight
            ships = 1
            for w in weights:
                if curr_capacity - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    curr_capacity = max_weight
                curr_capacity -= w
            return True

        while left <= right:
            mid = left + (right -left) // 2

            if canShip(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

            