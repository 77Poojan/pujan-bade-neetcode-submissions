class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def split(value):
            threshold = value
            total = 0
            maxx = 0

            for num in nums:
                if total - num < 0:
                    maxx += 1
                    if maxx > k:
                        return False
                    total = threshold
                    
                total -= num

            return True
                


        l = max(nums)
        r = sum(nums)
        res = r

        while l <= r:
            mid = l + (r - l) // 2
            
            summ = split(mid)
            
            if summ:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res