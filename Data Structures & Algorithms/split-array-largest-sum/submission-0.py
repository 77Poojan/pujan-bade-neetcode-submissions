class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(largest):
            subarray = 0
            curr = 0
            for n in nums:
                curr += n
                if curr > largest:
                    subarray += 1
                    curr = n
            return subarray + 1 <= k

        l = max(nums)
        r = sum(nums)
        res = r

        while l <= r:
            mid = l + ((r - l) // 2)
            if can_split(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res