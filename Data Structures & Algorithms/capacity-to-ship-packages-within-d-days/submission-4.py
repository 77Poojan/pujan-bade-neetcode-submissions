class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        def can_ship(threshold):
            ship, curr_capacity = 1, threshold
            for weight in weights:
                if curr_capacity - weight < 0:
                    ship += 1
                    if ship > days:
                        return False
                    curr_capacity = threshold
                curr_capacity -= weight
            return True

        while left <= right:
            mid = left + (right - left) // 2

            if can_ship(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


