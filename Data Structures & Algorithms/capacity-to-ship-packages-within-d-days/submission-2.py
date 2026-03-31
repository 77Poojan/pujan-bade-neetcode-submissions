class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def validate(threshold):
            ships, currCap = 1, threshold
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = threshold 
                currCap -= w 
            return True

        while l <= r:
            mid = l + ((r - l) // 2)
            if validate(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res