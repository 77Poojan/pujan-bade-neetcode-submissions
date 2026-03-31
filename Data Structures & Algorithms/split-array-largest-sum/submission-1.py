class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            summ = largest
            subarray = 1
            for num in nums:
                if summ - num < 0:
                    subarray += 1
                    if subarray > k:
                        return False
                    summ = largest
                summ -= num
            return True
        

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res